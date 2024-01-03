import os

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException

from .nytimes_client import get_top_stories
from .story_formatter import format_stories_to_string
from .summarizer import summarize_news_stories

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"msg": "Welcome to my app"}


@app.get("/news")
def news():
    summary = ""
    images = []
    try:
        stories = get_top_stories()
        for story in stories:
            images.extend(story["multimedia"])
        summary = summarize_news_stories(format_stories_to_string(stories))
        images = list(
            filter(lambda image: image["format"] == "Large Thumbnail", images)
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, detail="Apologies, something bad happened :("
        )
    return {"summary": summary, "images": images}