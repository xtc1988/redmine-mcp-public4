import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_search(monkeypatch):
    async def mock_search_issues(self, params):
        return {"issues": [{"id": 1, "subject": "test"}]}
    monkeypatch.setattr("redmine_client.RedmineClient.search_issues", mock_search_issues)
    resp = client.post("/search", json={"params": {"project_id": 1}})
    assert resp.status_code == 200
    assert resp.json()["issues"][0]["id"] == 1

def test_update(monkeypatch):
    async def mock_update_issue(self, issue_id, data):
        return {"issue": {"id": issue_id, **data}}
    monkeypatch.setattr("redmine_client.RedmineClient.update_issue", mock_update_issue)
    resp = client.post("/update", json={"issue_id": 1, "data": {"subject": "updated"}})
    assert resp.status_code == 200
    assert resp.json()["issue"]["subject"] == "updated"
