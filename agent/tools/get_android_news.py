from agents import function_tool
import feedparser
import traceback

from agents import function_tool
import traceback
from utils.rss_helper import fetch_rss_feed

@function_tool
def get_android_news(limit: int = 5) -> str:
    print("In get_android_news")

    try:
        return fetch_rss_feed(
            "https://android-developers.googleblog.com/feeds/posts/default",
            limit
        )

    except Exception as e:
        print("Error in get_android_news:")
        traceback.print_exc()
        return f"Error fetching Android news: {e}"