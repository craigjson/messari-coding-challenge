from typing import Dict, List
from data.models.article import  Article
from data.query import query_articles, query_article, delete_article, query_articles_by_pattern_id

# Get all articles
def get_all_articles() -> List[Article]:
    return query_articles()

def get_articles_for_pattern(pattern_id: str) -> List[Article]:
    return query_articles_by_pattern_id(pattern_id)

# Get Article By Id
def get_article_by_id(article_id: str) -> Article:
    return query_article(article_id)
    
# Delete Article by Id
def delete_article(article_id: str):
    return delete_article(article_id)
    