from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .selenium_utils import get_page_title

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scrape/")
def scrape(url: str):
    title = get_page_title(url)
    return {"title": title}
