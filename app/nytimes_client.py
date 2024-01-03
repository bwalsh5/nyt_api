import os
API_KEY = os.environ.get("NYTIMES_API_KEY")
from pynytimes import NYTAPI
nyt = NYTAPI(API_KEY, parse_dates=True)

def get_top_stories():
    return nyt.top_stories()