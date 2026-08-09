from agents import function_tool
import feedparser
import traceback

from agents import function_tool
import traceback
from utils.rss_helper import fetch_rss_feed

@function_tool
def get_compose_news(limit: int = 5) -> str:
    print("In get_compose_news")

    try:
        return fetch_rss_feed(
            "https://developer.android.com/feeds/androidx-release-notes.xml",
            limit
        )

    except Exception as e:
        print("Error in get_compose_news:")
        traceback.print_exc()
        return f"Error fetching get_compose_news : {e}"