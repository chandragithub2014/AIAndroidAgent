from agents import function_tool
from utils.rss_helper import fetch_rss_feed

@function_tool
def get_firebase_news(limit: int = 5) -> str:
    """
    Fetches the latest news and updates from the official Firebase RSS blog feed.

    Args:
        limit (int): The maximum number of news articles to fetch. Defaults to 5.

    Returns:
        str: A string containing the formatted RSS feed articles or an error message.
    """
    print("******** FIREBASE TOOL CALLED ********")
    try:
        return fetch_rss_feed(
            "https://firebase.blog/rss.xml",
            limit
        )
    except Exception as e:
        print("Error in get_firebase_news:")
        traceback.print_exc()
        return f"Error fetching get_firebase_news : {e}"    