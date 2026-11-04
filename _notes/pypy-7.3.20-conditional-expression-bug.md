# PyPy 3.11 v7.3.20 の条件式バグ

AtCoder の「Python (PyPy 3.11-v7.3.20)」で、副作用のある条件式を文として書くと、両方の分岐が実行されることがある。
CPython と Codon では起きない。PyPy 8.0.1 では直っている。

## 実際の提出

- 提出: https://atcoder.jp/contests/adt_all_20261104_2/submissions/80593818
- 問題: [ABC326 A - 2UP3DOWN](https://atcoder.jp/contests/adt_all_20261104_2/tasks/abc326_a)
- 言語: Python (PyPy 3.11-v7.3.20)
- 結果: WA（hand_01, random_04, random_05, random_11, sample_02）

```python
X, Y = read_integers()


if X < Y:
    print("Yes") if Y - X <= 2 else print("No")
else:
    print("Yes") if X - Y <= 3 else print("No")
```

ロジックは正しい。`else` 側の末尾の条件式が真になる入力（`9 6` など、下りで Yes になるケース）で `Yes` と `No` の2行が出力されて WA になった。
コードテストでは、CPython と Codon は `Yes`、PyPy 3.11-v7.3.20 だけが `Yes` `No` を出力した。

## 再現コード

```python
x = True
if x:
    print("Yes") if x else print("No")
```

v7.3.20 での出力（本来は `Yes` のみ）:

```
Yes
No
```

同じ位置に `and` / `or` を置くと、実行前のコンパイルでクラッシュする（RE になる）。

```python
x = True
if x:
    x or x
```

```
File "pypy_interpreter_astcompiler.c", in PythonCodeMaker_optimize_unreachable_code
Fatal RPython error: AssertionError
```

## 発生条件（v7.3.20 で実測）

1. `if` ブロックの中にある（`if 1:` のような定数条件でも起きる）
2. そのブロックの最後の文が、条件式の文になっている（条件が定数なら起きない）
3. その後ろがコード末尾になっている（後ろに文が続けば起きない）

| 書き方 | 7.3.20 |
|---|---|
| `else` の末尾（モジュール直下・関数内） | Yes / No |
| `else` のない `if` の末尾 | Yes / No |
| `else` のある `if` 節の末尾 | Yes |
| 後ろに文が続く | Yes |
| `for` の中 | Yes |
| トップレベルに単独で書く | Yes |
| `print("Yes" if c else "No")` | Yes |

## 原因の見立て

バイトコードを見ると、真の分岐の後にある「偽の分岐を飛び越えるジャンプ」が消えている。

```
22 POP_JUMP_IF_FALSE  (to 32)
24 LOAD_NAME  print
26 LOAD_CONST 'Yes'
28 CALL_FUNCTION 1
30 POP_TOP
                       ← ここにあるべき JUMP がない
32 LOAD_NAME  print
34 LOAD_CONST 'No'
36 CALL_FUNCTION 1
```

クラッシュも同じ最適化 `optimize_unreachable_code` の中で起きている。
ジャンプ先が末尾の暗黙の `return None` になるブロックを処理するときに、ジャンプを壊していると見ている。

## 教訓

- 副作用のある処理を条件式で分岐させない。値を選ぶ形にする: `print("Yes" if c else "No")`
- `_yes_no` スニペットはこの形に修正済み。
- 手元と提出先で結果が違うときは、処理系のバージョンを揃えて確認する。
  PyPy の旧版は `https://downloads.python.org/pypy/` から取得できる（uv の管理対象外）。
