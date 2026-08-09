# test_downloader.py

from agent.docs.crawler.android_crawler import download_page

def test_download():
    url = "https://developer.android.com/topic/libraries/architecture/workmanager"

    content = download_page(url)

    print(content[:3000])

if __name__ == "__main__":
    test_download()