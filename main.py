import configparser
import requests
import sys
import json

class RedmineClient:
    def __init__(self, config_path='config.ini'):
        config = configparser.ConfigParser()
        config.read(config_path, encoding='utf-8')
        self.url = config['redmine']['url'].rstrip('/')
        self.api_key = config['redmine']['api_key']
        self.headers = {'X-Redmine-API-Key': self.api_key, 'Content-Type': 'application/json'}

    def search_issues(self, **params):
        """課題を検索する。paramsはRedmine APIのクエリパラメータ"""
        response = requests.get(f"{self.url}/issues.json", headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def update_issue(self, issue_id, update_data):
        """課題を全項目更新する。update_dataはdictで全項目指定"""
        response = requests.put(f"{self.url}/issues/{issue_id}.json", headers=self.headers, data=json.dumps({'issue': update_data}))
        response.raise_for_status()
        return response.json()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [search|update] <args>")
        sys.exit(1)
    mode = sys.argv[1]
    client = RedmineClient('config.ini')

    if mode == 'search':
        # 例: python main.py search project_id=1 status_id=*
        params = dict(arg.split('=') for arg in sys.argv[2:])
        result = client.search_issues(**params)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif mode == 'update':
        # 例: python main.py update 123 update.json
        if len(sys.argv) != 4:
            print("Usage: python main.py update <issue_id> <update_json_file>")
            sys.exit(1)
        issue_id = sys.argv[2]
        with open(sys.argv[3], encoding='utf-8') as f:
            update_data = json.load(f)
        result = client.update_issue(issue_id, update_data)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("Unknown mode")
        sys.exit(1)

if __name__ == '__main__':
    main()
