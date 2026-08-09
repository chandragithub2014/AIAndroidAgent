from agents import function_tool
from utils.rss_helper import fetch_rss_feed

@function_tool
def get_kotlin_news(limit: int = 5) -> str:
    print("In get_kotlin_news")
    try:
        return fetch_rss_feed(
            "https://blog.jetbrains.com/kotlin/feed/",
            limit
        )
    except Exception as e:
        print("Error in get_kotlin_news:")
        traceback.print_exc()
        return f"Error fetching get_kotlin_news : {e}"    