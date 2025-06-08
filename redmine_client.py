import httpx

class RedmineClient:
    def __init__(self, url: str, api_key: str):
        self.url = url.rstrip('/')
        self.api_key = api_key
        self.headers = {"X-Redmine-API-Key": api_key}

    async def search_issues(self, params: dict):
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{self.url}/issues.json", params=params, headers=self.headers)
            resp.raise_for_status()
            return resp.json()

    async def update_issue(self, issue_id: int, data: dict):
        async with httpx.AsyncClient() as client:
            resp = await client.put(f"{self.url}/issues/{issue_id}.json", json=data, headers=self.headers)
            resp.raise_for_status()
            return resp.json()
