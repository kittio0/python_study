from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class post(BaseModel):
    text: str

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
}

@app.get("/api/profile")
def get_profile():
    return profile

@app.post("/api/analyze")
def analyze(p:post):
    return {
        "text":p.text,
        "status":200  
        }
