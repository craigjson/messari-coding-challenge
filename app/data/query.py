from typing import List

from data.models.article import Article
from data.models.article_pattern_match import ArticlePatternMatch
from data.models.news_source import NewsSource
from data.models.pattern import Pattern

from .postgres import Session

## Article Queries

# Get All Articles
def query_articles() -> List[Article]:
    session = Session()
    articles = session.query(Article).all()
    session.close() 
    return list(articles)

# Get Article by Id
def query_article(id: str) -> Article:
    session = Session()
    article = session.query(Article).filter(Article.id == id).first()
    session.close() 
    return article

# Get Article by Title
def query_article_by_title(title: str) -> Article:
    session = Session()
    article = session.query(Article).filter(Article.title == title).first()
    session.close()
    return article

# Get Article by URL
def query_article_by_title(url: str) -> Article:
    session = Session()
    article = session.query(Article).filter(Article.url == url).first()
    session.close()
    return article

# Create Article and save to DB
def save_articles(articles: List[Article]):
    session = Session()
    [session.add(article) for article in articles]
    session.commit()
    session.close()

# Create Article and save to DB
def save_article(article: Article):
    session = Session()
    session.add(article)
    session.commit()
    session.close()
    
# Delete Article by Id
def delete_article(id: str):
    session = Session()
    article = session.query(Article).filter(Article.id == id).first()
    session.delete(article)
    session.commit()
    session.close()

## News Source Queries

# Save News Source
def save_news_source(news_source: NewsSource):
    session = Session()
    session.add(news_source)
    session.commit()
    session.close()

# Get All News Sources
def query_news_sources() -> List[NewsSource]:
    session = Session()
    news_sources = session.query(NewsSource).all()
    session.close() 
    return list(news_sources)

# Get News Source by Id
def query_news_source(id) -> NewsSource:
    session = Session()
    news_source = session.query(NewsSource).filter(NewsSource.id == id).first()
    session.close()
    return news_source
    
# Update News Source
def update_news_source(news_source: NewsSource):
    session = Session()
    session.query(NewsSource).filter(NewsSource.id == news_source.id).\
        update({
            NewsSource.url: news_source.url, 
            NewsSource.last_processed: news_source.last_processed, 
            NewsSource.status: news_source.status.value})
    session.commit()
    session.close()

# Delete News Source
def delete_news_source(id: str):
    session = Session()
    news_source = session.query(NewsSource).filter(NewsSource.id == id).first()
    session.delete(news_source)
    session.commit()
    session.close()

## Pattern Queries

# Create Pattern
def save_pattern(pattern: Pattern):
    session = Session()
    session.add(pattern)
    session.commit()
    session.close()

# Get All Patterns
def query_patterns() -> List[Pattern]:
    session = Session()
    patterns = session.query(Pattern).all()
    session.close()
    return list(patterns)

# Get Pattern by Id
def query_pattern(id: str) -> Pattern:
    session = Session()
    pattern = session.query(Pattern).filter(Pattern.id == id).first()
    session.close()
    return pattern
    
# Update Pattern
def update_pattern(pattern: Pattern):
    session = Session()
    session.query(Pattern).filter(Pattern.id == pattern.id).update({
        Pattern.regex: pattern.regex, 
    })
    session.commit()
    session.close()
    
# Delete Pattern
def delete_pattern(id: str):
    session = Session()
    pattern = session.query(Pattern).filter(Pattern.id == id).first()
    session.delete(pattern)
    session.commit()
    session.close()
    
# Article Pattern Match Queries

# Create Article Pattern Match
def save_article_pattern_match(article_pattern_match: ArticlePatternMatch):
    session = Session()
    session.add(article_pattern_match)
    session.commit()
    session.close()
    
# Get All Article Pattern Matches
def get_pattern_matches() -> List[ArticlePatternMatch]:
    session = Session()
    pattern_matches = session.query(ArticlePatternMatch).all()
    session.close()
    return list(pattern_matches)

# Get All Patterns for Article Id
def get_patterns_matches_for_article(article_id: str) -> List[ArticlePatternMatch]:
    session = Session()
    pattern_matches = session.query(ArticlePatternMatch).filter(ArticlePatternMatch.article_id == article_id).all()
    session.close()
    return list(pattern_matches)

# Get All Articles for Pattern Id
def get_article_matches_for_pattern(pattern_id: str) -> List[ArticlePatternMatch]:
    session = Session()
    pattern_matches = session.query(ArticlePatternMatch).filter(ArticlePatternMatch.pattern_id == pattern_id).all()
    session.close()
    return list(pattern_matches)