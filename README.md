# Redmine MCPサーバー (FastAPI版)

## 概要
Redmineの課題検索・更新をAPI経由で行うMCPサーバーです。

## インストール
```sh
pip install -r requirements.txt
```

## 設定
`.env` または `settings.json` をプロジェクトルートに配置し、RedmineのURLとAPIキーを設定してください。

## 起動方法
```sh
uvicorn main:app --reload
```

## API仕様
- `/search` : 課題検索API
- `/update` : 課題更新API

## テスト
```sh
pytest
```
