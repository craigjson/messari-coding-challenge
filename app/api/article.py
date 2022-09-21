from typing import Dict, List
from data.models.article import  Article
from data.query import query_articles, query_article, delete_article, query_articles_without_matches

# Get all articles
def get_all_articles() -> List[Article]:
    return query_articles()

# Get Article By Id
def get_article_by_id(article_id: str) -> Article:
    return query_article(article_id)
    
# Delete Article by Id
def delete_article(article_id: str):
    return delete_article(article_id)

def get_articles_with_no_match() -> List[Article]:
    return query_articles_without_matches()
    