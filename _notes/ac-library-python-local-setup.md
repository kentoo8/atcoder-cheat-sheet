# ローカルPythonでのac-library-python利用

## 確認した環境

- 確認日: 2026-11-15
- macOS 27.2.1 / Apple Silicon
- Python 3.14.10（uv管理、`~/.local/bin/python`）
- uv 0.13.8
- ac-library-python 0.1.0

このリポジトリには `pyproject.toml`、`uv.lock` はなく、VS Codeはsystem環境を使用する設定。
既存の `.venv` には `bin/python` と `pyvenv.cfg` がないため、通常の `python` が使うユーザー用Pythonへ追加した。
設定やディレクトリ構成は変更していない。

## 導入と実行

```sh
uv pip install --python "$(command -v python)" --break-system-packages ac-library-python==0.1.0
python 0.py < 0-input.txt
```

`--break-system-packages` は、今回のuv管理Pythonがexternally managedとして直接の追加を保護しているために使用した。
再導入時は `python -c 'import sys; print(sys.executable); print(sys.prefix)'` で追加先を確認する。
Pythonを別バージョンへ切り替えた場合、その環境にも導入する必要がある。

配布名は `ac-library-python`、インポート名は `atcoder`。
AtCoderで使用する `from atcoder.maxflow import MFGraph` をそのまま使える。
AtCoderの処理系やライブラリバージョンとの一致までは確認していない。

## 動作確認

```python
from atcoder.maxflow import MFGraph

g = MFGraph(4)
for edge in [(0, 1, 2), (0, 2, 1), (1, 2, 1), (1, 3, 1), (2, 3, 2)]:
    g.add_edge(*edge)
assert g.flow(0, 3) == 3
```

上記のインポートと最大流3を確認した。
手元の `0.py` と `0-input.txt` によるサンプル実行結果は `13`。
サンプルの内容は変更せず、今回のコミットにも含めない。

## Pylanceでインポートが解決できない場合

2026-11-15のVS Codeログでは、このワークスペースのPylanceは
`~/.local/bin/python3.12`（Python 3.12.16）を参照していた。
実行時のPython 3.14.10とは異なるため、実行に成功してもエディタには
`reportMissingImports` が表示される。

VS Codeで `Python: Select Interpreter` → `Enter interpreter path...` を開き、
`command -v python` の出力する絶対パスを指定して実行環境と揃える。
診断が残る場合は `Developer: Reload Window` を実行する。
インタープリターを揃えた後、ユーザーが警告の解消を確認した。

Pylanceはワークスペースで選択したPythonのライブラリを検索する。
既に選択済みの環境は `python.defaultInterpreterPath` の追加だけでは切り替わらない場合があるため、
インタープリターを選び直す。
参照: [Pylanceの公式環境選択ガイド](https://github.com/microsoft/pylance-release/blob/main/docs/howto/python-environments.md)。
