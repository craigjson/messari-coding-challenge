from typing import Dict, List
from ..models.models import  Article
from ..data.data import articles

# Get all articles
def get_all_articles() -> Dict[str, Article]:
    return articles

# Get Article By Id
def get_article_by_id(article_id: str) -> Article:
    return articles[article_id]
    
# Delete Article by Id
def delete_article(article_id: str):
    del articles[article_id]