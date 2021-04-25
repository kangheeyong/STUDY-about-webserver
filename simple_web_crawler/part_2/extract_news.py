import argparse
import requests
from datetime import datetime

import feedparser


def _get_url(query: str, day: int = 1) -> str:
    return f"https://news.google.com/rss/search?q={query}+when:{day}d&hl=ko&gl=KR&ceid=KR:ko"


def _get_search_result(url: str):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text


def get_search_result(query: str):
    url = _get_url(query)
    text = _get_search_result(url)

    data = feedparser.parse(text).entries

    result = [(d.title, datetime(*d.published_parsed[:6]), d.link) for d in data]
    result.sort(key=lambda x: x[1], reverse=True)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="news search query")
    args = parser.parse_args()
    query = args.query
    for r in get_search_result(query):
        print(f"title: {r[0]}, date: {r[1]}, url: {r[2]}")


if __name__ == "__main__":
    main()
