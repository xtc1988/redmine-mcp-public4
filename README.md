# Redmine MCP

Redmineの課題検索・全項目更新ツール

## 概要
RedmineのREST APIを利用し、課題の検索・全項目更新をコマンドラインから実行できます。

## セットアップ手順（他PCでもOK）
1. Python 3.8以上をインストール
2. このリポジトリをクローン
3. `requirements.txt` で依存パッケージをインストール
   ```
   pip install -r requirements.txt
   ```
4. `config.sample.ini` を `config.ini` にコピーし、RedmineのURLとAPIキーを記入
   ```
   copy config.sample.ini config.ini  # Windows
   # または
   cp config.sample.ini config.ini    # Mac/Linux
   ```
5. `main.py` を実行

## 使い方

### 課題検索
```
python main.py search project_id=1 status_id=*
```

### 課題更新
```
python main.py update <issue_id> <update_json_file>
```

例：
```
python main.py update 123 update.json
```

`update.json` にはRedmine API仕様に従った課題項目を記載してください。

---

## 設定ファイル例

`config.sample.ini` を参考に `config.ini` を作成してください。

```
[redmine]
url = https://your-redmine-url/
api_key = your_api_key_here
```

## トラブルシュート
- 認証エラー：APIキーやURLを再確認
- SSLエラー：Redmineサーバーの証明書設定を確認
- その他APIエラー：レスポンス内容を確認

## GitLabへのpush方法
1. GitLabで新規リポジトリを作成
2. このディレクトリで初回push
   ```
   git init
   git remote add origin <GitLabのリポジトリURL>
   git add .
   git commit -m "first commit"
   git push -u origin master
   ```

## 注意
- `config.ini`は個人情報を含むため、Git管理対象外です（.gitignore済み）
