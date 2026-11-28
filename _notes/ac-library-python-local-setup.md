# ローカルPythonでのac-library-python利用

配布名は `ac-library-python`、インポート名は `atcoder`。
依存関係はリポジトリの `pyproject.toml` と `uv.lock` で管理する。

## 実行と確認

リポジトリのルートで実行する。

```sh
uv run --locked python セグメント木/0.py < セグメント木/0-input.txt
```

出力は `3`、`3`、`2`、`6` が1行ずつ。
使用するPythonとライブラリの場所は次のコマンドで確認できる。

```sh
uv run --locked python -c 'import sys, atcoder.segtree; print(sys.executable); print(atcoder.segtree.__file__)'
```

## VS Codeで補完やデバッグに使う

初回の `uv run` で `.venv` を作った後、**Python: Select Interpreter** で
プロジェクトの `.venv` を選ぶ。選択した環境は補完やデバッグに使われる。
統合ターミナルで直接入力する `python` は、シェルが見つけた実行ファイルを使う。
ターミナルで実行するときは `uv run` を使うと、仮想環境の手動有効化が不要になる。
