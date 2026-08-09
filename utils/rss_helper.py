import feedparser

def fetch_rss_feed(url: str, limit: int = 5) -> str:
    feed = feedparser.parse(url)

    result = ""

    for entry in feed.entries[:limit]:

        published = (
            getattr(entry, "published", None)
            or getattr(entry, "updated", None)
            or getattr(entry, "published_parsed", None)
            or "No date available"
        )

        result += f"""
Title: {entry.title}
Published: {published}
Link: {entry.link}

"""

    return result