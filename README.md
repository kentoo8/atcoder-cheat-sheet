# atcoder-cheat-sheet

AtCoder用の個人チートシートです。Pythonのコード例、学習メモ、VS Code用スニペットを置いています。

- `0.py`, `0-input.txt`：問題を解くための作業用ファイル。
  `uv run --locked python 0.py < 0-input.txt` で実行します。
- 各フォルダ：アルゴリズムや標準ライブラリのコード例
- `.vscode/python.code-snippets`：Python用スニペット

学習・試行途中のコードを含みます。

## ローカル実行

[uv](https://docs.astral.sh/uv/getting-started/installation/) をインストールし、クローンしたリポジトリで実行します。初回は uv がプロジェクトの `.venv` を作り、`uv.lock` に沿って依存ライブラリをインストールします。

各フォルダのコード例も同じように実行できます。

```sh
cd セグメント木
uv run --locked python 0.py < 0-input.txt
```

VS Code で補完やデバッグに使う Python は、初回実行後に **Python: Select Interpreter** でプロジェクトの `.venv` を選びます。

## License

[MIT-0](LICENSE)。自由に利用・改変・再配布・販売できます。著作者表示・ライセンス文の同梱・連絡は不要です。
