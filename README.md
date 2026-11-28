# atcoder-cheat-sheet

AtCoder用の個人チートシートです。Pythonのコード例、学習メモ、VS Code用スニペットを置いています。

- `0.py`, `0-input.txt`：問題を解くための作業用ファイル。
  `uv run python 0.py < 0-input.txt` で実行します。
- 各フォルダ：アルゴリズムや標準ライブラリのコード例
- `.vscode/python.code-snippets`：Python用スニペット

学習・試行途中のコードを含みます。

## ローカル実行

[uv](https://docs.astral.sh/uv/getting-started/installation/) をインストールし、クローンしたリポジトリで実行します。初回は uv がプロジェクトの `.venv` を作り、`uv.lock` に沿って依存ライブラリをインストールします。

各フォルダのコード例も同じように実行できます。

```sh
cd セグメント木
uv run python 0.py < 0-input.txt
```

VS Code で補完やデバッグに使う Python は、初回実行後に **Python: Select Interpreter** でプロジェクトの `.venv` を選びます。

## ライブラリの更新

提出に使う Python や PyPy で、AtCoder が用意しているライブラリだけを使います。
年に1回を目安に、また Python や PyPy の環境更新のお知らせが出たときに、使っているライブラリのバージョンを確認します。
[AtCoder の重要な告知](https://atcoder.jp/important-posts?lang=ja)

AtCoder 側で使っているライブラリのバージョンが変わったら、`pyproject.toml` の指定を合わせて、上のサンプルを実行します。
そのとき uv が `uv.lock` も更新するので、両方のファイルをコミットします。

## License

[MIT-0](LICENSE)。自由に利用・改変・再配布・販売できます。著作者表示・ライセンス文の同梱・連絡は不要です。
