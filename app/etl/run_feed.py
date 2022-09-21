from datetime import datetime
from typing import List

from api.news_source import get_sources
from data.models.news_source import NewsSource
from data.query import update_news_source
from util.crawl import CrawlStatus

from etl.parser import parse_news_source


# Run ETL Feed
def extract_transform_load_feed():
    try:
        # Retrieve news source URLs from the Database
        news_sources: List[NewsSource] = get_sources()
        
        articles = []
        # Parse News Sources for Articles
        for news_source in news_sources:
            try:
                articles.extend(parse_news_source(news_source))
                update_news_source(
                    news_source.id, 
                    news_source.url, 
                    datetime.now(),
                    CrawlStatus.SUCCESS.value
                )
            except Exception as e:
                print(f"Failed to parse news source with\nError: {e}\n")
                update_news_source(
                    news_source.id, 
                    news_source.url, 
                    datetime.now(),
                    CrawlStatus.FAILED.value
                )
                continue
        print(f"Total Articles Matched: {len(articles)}")
        
        # Load articles into the Database
        #load_articles_into_postgres(articles)
    except Exception as e:
        print(f"Error running ETL Feed: {e}")
