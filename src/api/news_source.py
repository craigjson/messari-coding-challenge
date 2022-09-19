from ..data.mock_data import news_sources
from ..data.models import NewsSource, Pattern
from ..data.query import query_news_sources, query_news_source, save_news_source, update_news_source, delete_news_source
from typing import Dict, List

## Create News Source
def create_news_source(source_id: str, url: str, patterns: List[Pattern]):
    save_news_source(source_id, url, patterns)

## Get NewsSource by Id
def get_source(source_id: str) -> NewsSource:
    return query_news_source(source_id)

## Get All NewsSources
def get_sources() -> List[NewsSource]:
    return query_news_sources()

## Update NewsSource
def update_source(source_id: str, url: str, patterns: List[Pattern]):
    update_news_source(source_id, url, patterns)

## Delete NewsSource
def delete_source(source_id: str):
    delete_news_source(source_id)