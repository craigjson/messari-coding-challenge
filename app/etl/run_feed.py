from datetime import datetime
from typing import List

from data.query import query_news_source, query_news_sources
from data.models.article import Article
from data.models.news_source import NewsSource
from data.query import update_news_source
from util.crawl import CrawlStatus

from etl.source_parser import parse_news_source

def run_etl_for_single_source(source_id: str) -> List[Article]:
    news_source: NewsSource = query_news_source(source_id)
    try:
        articles: List[Article] = parse_news_source(news_source)
        news_source.status = CrawlStatus.SUCCESS
        news_source.last_processed = datetime.now()
        update_news_source(news_source)
        return articles
    except Exception as e:
        print(f"Failed to parse news source: {news_source.url} with\nError: {e}\n")
        news_source.status = CrawlStatus.FAILED
        news_source.last_processed = datetime.now()
        update_news_source(news_source)
    
    return []

# Run ETL Feed
def extract_transform_load_feed():
    try:
        # Retrieve news source URLs from the Database
        news_sources: List[NewsSource] = query_news_sources()
        
        articles = []
        # Parse News Sources for Articles
        for news_source in news_sources:
            try:
                articles.extend(parse_news_source(news_source))
                news_source.status = CrawlStatus.SUCCESS
                news_source.last_processed = datetime.now()
                update_news_source(news_source)
                print(f"Successfully parsed news source: {news_source.url}\n")
            except Exception as e:
                print(f"Failed to parse news source {news_source.id} with\nError: {e}\n")
                news_source.status = CrawlStatus.FAILED
                news_source.last_processed = datetime.now()
                update_news_source(news_source)
                continue
            
        log_matched_articles_to_console(articles)
        
        # Load articles into the Database
        #load_articles_into_postgres(articles)
    except Exception as e:
        print(f"Error running ETL Feed: {e}")

def log_matched_articles_to_console(articles: List[Article]):
    for article in articles:
        if article.has_match:
            print()
            print(f"Title: {article.title}")
            print(f"Published: {article.published}")
            print(f"Content: {article.content}")