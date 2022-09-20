from typing import Dict, List
from data.models import  Article
from data.mock_data import articles
from data.query import query_articles, query_artcile

# Get all articles
def get_all_articles() -> List[Article]:
    return query_articles()

# Get Article By Id
def get_article_by_id(article_id: str) -> Article:
    return query_artcile(article_id)
    
# Delete Article by Id
def delete_article(article_id: str):
    del articles[article_id]