from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import get_settings
from redmine_client import RedmineClient

app = FastAPI()

settings = get_settings()
redmine = RedmineClient(settings["redmine_url"], settings["redmine_api_key"])

class SearchRequest(BaseModel):
    params: dict

class UpdateRequest(BaseModel):
    issue_id: int
    data: dict

@app.post("/search")
async def search_issues(req: SearchRequest):
    try:
        result = await redmine.search_issues(req.params)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/update")
async def update_issue(req: UpdateRequest):
    try:
        result = await redmine.update_issue(req.issue_id, req.data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
