# Redmine MCP

Redmineの課題検索・全項目更新ツール

---

## 【Windows＋VSCode＋GitHub Copilot（MCP/AIアシスタント）利用者向け】

### 1. 必要なもの
- Windows PC
- [VSCode（Visual Studio Code）](https://code.visualstudio.com/)（最新版推奨）
- [GitHubアカウント](https://github.com/)
- [GitHub Copilot Chat（MCP/AIアシスタント）拡張機能](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)
- Python 3.8以上
- Git（[公式ダウンロード](https://git-scm.com/)）

---

### 2. セットアップ手順

#### 2-1. VSCodeのインストール
- [公式サイト](https://code.visualstudio.com/)からダウンロードし、インストール

#### 2-2. Gitのインストール
- [公式サイト](https://git-scm.com/)からダウンロードし、インストール
- インストール後、コマンドプロンプトで `git --version` で動作確認

#### 2-3. Pythonのインストール
- [公式サイト](https://www.python.org/downloads/)からダウンロードし、インストール
- インストール後、コマンドプロンプトで `python --version` で動作確認

#### 2-4. リポジトリのクローン
1. VSCodeを起動
2. 「表示」→「ターミナル」からターミナルを開く
3. 下記コマンドを実行
   ```sh
   git clone https://github.com/xtc1988/redmine-mcp-public4.git
   cd redmine-mcp-public4
   ```

#### 2-5. Python仮想環境（推奨）
```sh
python -m venv venv
venv\Scripts\activate
```

#### 2-6. 依存パッケージのインストール
```sh
pip install -r requirements.txt
```

#### 2-7. 設定ファイルの作成
```sh
copy config.sample.ini config.ini
```
- `config.ini`をエディタで開き、RedmineのURLとAPIキーを記入

---

### 3. GitHub Copilot Chat（MCP/AIアシスタント）の使い方

1. VSCode左側の拡張機能から「GitHub Copilot Chat」をインストール
2. サイドバーのCopilotアイコンをクリックし、チャット欄を開く
3. 例：「main.pyを実行してRedmineの課題を検索したい」など自然言語で指示
4. 実際にコマンドを打つ場合は、ターミナルで下記を実行

#### 3-1. 課題検索
```sh
python main.py search project_id=1 status_id=*
```

#### 3-2. 課題更新
```sh
python main.py update <issue_id> <update_json_file>
```
例：
```sh
python main.py update 123 update.json
```

---

### 4. よくあるトラブルと対策
- `pip`や`python`コマンドが見つからない → パス設定や再インストールを確認
- `config.ini`のAPIキーやURLが間違っている → 正しい値を再確認
- RedmineサーバーのSSL証明書エラー → サーバー管理者に確認

---

### 5. 参考
- [GitHub Copilot Chat公式ドキュメント](https://docs.github.com/ja/copilot/getting-started-with-github-copilot/getting-started-with-github-copilot-in-visual-studio-code)
- [Redmine REST API公式ドキュメント](https://www.redmine.org/projects/redmine/wiki/Rest_api)

---

このREADMEの手順通りに進めれば、**VSCode＋GitHub Copilot Chat（MCP/AIアシスタント）環境でRedmine MCPを利用できます**。

何か問題があれば、Copilot Chatに「エラー内容を教えて」などと質問してください。
