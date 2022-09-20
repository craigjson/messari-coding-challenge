# Load Articles into PostgresSQL
from typing import List
from models.models import Article
from ..data.query import create_article

## Load Article into PostgresSQL
def load_article_into_postgres(id: str, title: str, content: str, published: str):
    create_article(id, title, content, published)
    
def load_articles_into_postgres(articles: List[Article]):
    for article in articles:
        load_article_into_postgres(article.id, article.title, article.content, article.published)