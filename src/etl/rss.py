# Get all RSS Entries for all news sources
from ast import List
from typing import Dict
from feedparser import parse, FeedParserDict
from ..api.news_source import get_sources
from ..models.models import NewsSource

def extract_all_feeds_from_source_urls() -> list:
    news_sources: Dict[str, NewsSource] = get_sources()
    return extract_all_rss_entries([news_source.url for news_source in news_sources.values()])

def extract_all_rss_entries(rss_feeds: List[str]) -> list:
    return [parse(url)['entries'] for url in rss_feeds]