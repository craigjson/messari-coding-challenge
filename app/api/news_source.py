from datetime import datetime
from typing import List

from data.models.news_source import NewsSource
from data.query import (delete_news_source, query_news_source,
                        query_news_sources, save_news_source)
from etl.source_parser import parse_news_source
from util.crawl import CrawlStatus
from util.url_cache import remove_from_url_visited_cache

from api.article import get_articles_for_news_source


## Create News Source
def create_news_source(source_id: str, url: str):
    news_source = NewsSource(
        id=source_id, 
        url=url, 
        last_processed=datetime.now(),
        status=CrawlStatus.NOT_STARTED.value
        )
    save_news_source(news_source)
    parse_news_source(news_source)

## Get NewsSource by Id
def get_source(source_id: str) -> NewsSource:
    return query_news_source(source_id)

## Get All NewsSources
def get_sources() -> List[NewsSource]:
    return query_news_sources()

## Update NewsSource by Id
## Implement as a delete and create to keep things simple even though it's not efficient
def update_source(news_source_id: str, url: str):
    delete_news_source(news_source_id.id)
    create_news_source(NewsSource(id=news_source_id, url=url))

## Delete NewsSource
def delete_source(source_id: str):
    # Delete will cascade and delete all articles and article pattern matches
    # that match this id. Due to this, we also need to remove all of the URLs 
    # from the cache so they can be properly reprocessed if the source is re-added
    articles = get_articles_for_news_source(source_id)
    delete_news_source(source_id)
    for article in articles:
        remove_from_url_visited_cache(article.id)
