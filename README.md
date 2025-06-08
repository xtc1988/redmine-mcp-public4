# Redmine MCPサーバー (FastAPI版)

## 概要
このプロジェクトは、Redmineの課題検索・更新をAPI経由で行う「MCPサーバー」です。

- VSCode Copilot、Cursor、ChatGPTなどのAIアシスタントから「Redmineの課題を検索して」「#1234の担当者を田中にして」など自然言語で指示するだけで、裏で自動的にRedmineと連携できます。
- エンドユーザーはAPIやコマンドを覚える必要はありません。

---

## 1. インストール手順

1. **リポジトリをクローン**
   ```sh
   git clone https://github.com/xtc1988/redmine-mcp-public4.git
   cd redmine-mcp-public4
   ```
2. **依存パッケージをインストール**
   ```sh
   pip install -r requirements.txt
   ```
3. **設定ファイルを作成**
   - `settings.json.sample` を `settings.json` にコピーし、RedmineのURLとAPIキーを記入
     ```json
     {
       "redmine_url": "https://your-redmine.example.com",
       "redmine_api_key": "xxxxxxxxxxxxxxxxxxxx"
     }
     ```
   - もしくは `.env` ファイルを作成し、以下のように記載
     ```env
     REDMINE_URL=https://your-redmine.example.com
     REDMINE_API_KEY=xxxxxxxxxxxxxxxxxxxx
     ```

---

## 2. サーバー起動

```sh
uvicorn main:app --reload
```
- デフォルトで http://127.0.0.1:8000 で待ち受けます。
- OpenAPIドキュメント（Swagger UI）は http://127.0.0.1:8000/docs で確認できます。

---

## 3. AIアシスタントでの使い方

- サーバーを起動した状態で、CopilotやCursor、ChatGPTなどのAIアシスタントに**自然言語で指示**してください。
  - 例：「RedmineのプロジェクトAの未完了チケットを一覧で出して」
  - 例：「#1234の課題の担当者を田中に変更して」
- AIが自動的にMCPサーバーAPIを呼び出し、Redmineとやりとりします。
- **エンドユーザーはAPI仕様やコマンドを意識する必要はありません。**

---

## 4. テスト

```sh
pytest test_main.py
```
- MCPサーバーAPIの自動テストが実行されます。

---

## 5. よくある質問・トラブルシューティング

- **Q. RedmineのURLやAPIキーが正しいのに動かない**
  - → サーバーのSSL証明書やネットワーク設定を確認してください。
- **Q. サーバーが起動しない／設定エラーになる**
  - → `.env`または`settings.json`の記述ミスがないか確認してください。
- **Q. AIアシスタントがMCPサーバーを認識しない**
  - → サーバーが起動しているか、AIの設定でMCPサーバーのURLが正しいか確認してください。

---

## 6. 開発・カスタマイズ

- API仕様の詳細は `/docs` で確認できます。
- コードはFastAPI＋httpxでシンプルに構成されています。
- テストはpytestで自動化されています。

---

## 7. AIアシスタント向け指示例

- 「このプロジェクトをインストールしてサーバーを起動して」
- 「Redmineの課題を検索して」
- 「#1234の課題の説明を“新しい説明”に更新して」

---

## ライセンス
MIT
