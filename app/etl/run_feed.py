from datetime import datetime
from typing import List

from data.models.article import Article
from data.models.news_source import NewsSource
from data.query import (query_news_source, query_news_sources, save_articles,
                        update_news_source)
from util.crawl import CrawlStatus

from etl.source_parser import parse_news_source


def run_etl_for_single_source(source_id: str=None, news_source: NewsSource=None) -> List[Article]:
    if not news_source:
        if source_id:
            news_source: NewsSource = query_news_source(source_id)
        else:
            raise Exception("No news source specified")
    try:
        parse_news_source(news_source)
        news_source.status = CrawlStatus.SUCCESS
        news_source.last_processed = datetime.now()
        update_news_source(news_source)
        print(f"Successfully parsed news source: {news_source.url}\n")
    except Exception as e:
        print(f"Failed to parse news source: {news_source.url} with\nError: {e}\n")
        news_source.status = CrawlStatus.FAILED
        news_source.last_processed = datetime.now()
        update_news_source(news_source)

# Run ETL Feed
def extract_transform_load_feed():
    try:
        # Retrieve news source URLs from the Database
        news_sources: List[NewsSource] = query_news_sources()
        
        # Parse News Sources for Articles
        for news_source in news_sources:
            run_etl_for_single_source(news_source=news_source)
    except Exception as e:
        print(f"Error running ETL Feed: {e}")
        
    print("Finished running ETL Feed")
