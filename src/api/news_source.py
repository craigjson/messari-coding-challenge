from ..data.data import news_sources
from ..models.models import NewsSource, Pattern
from typing import Dict, List

## Create News Source
def save_news_source(source_id: str, url: str, patterns: List[Pattern]):
    news_sources.append(NewsSource(
        id = source_id,
        url = url,
        patterns = patterns
    ))

## Get NewsSource by Id
def get_source(source_id: str):
   return news_sources[source_id]
    
## Get All NewsSources
def get_sources() -> Dict[str, NewsSource]:
   return news_sources

## Update NewsSource
def update_source(source_id: str, url: str, patterns: List[Pattern]):
    source = news_sources[source_id]
    source.url = url
    source.patterns = patterns

## Delete NewsSource
def delete_source(source_id: str):
    del news_sources[source_id]