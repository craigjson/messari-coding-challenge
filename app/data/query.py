from typing import List

from data.models.article import Article
from data.models.article_pattern_match import ArticlePatternMatch
from data.models.news_source import NewsSource
from data.models.pattern import Pattern
from data.postgres import Session


def getSession():
    db_session = Session()
    db_session.expire_on_commit = False
    return db_session

## Article Queries

# Get All Articles
def query_articles() -> List[Article]:
    session = getSession()
    articles = session.query(Article).all()
    return list(articles)

# Get Article by Id
def query_article(id: str) -> Article:
    session = getSession()
    article = session.query(Article).filter(Article.id == id).first()
    return article

def get_articles_by_id(ids: List[str]) -> List[Article]:
    session = getSession()
    articles = session.query(Article).filter(Article.id.in_(ids)).all()
    return list(articles)

# Get Article by Title
def query_article_by_title(title: str) -> Article:
    session = getSession()
    article = session.query(Article).filter(Article.title == title).first()
    return article

def query_articles_without_matches() -> List[Article]:
    session = Session()
    articles = session.query(Article).filter(Article.has_match == False).all()
    session.close()
    return list(articles)

# Get Article by URL
def query_article_by_title(url: str) -> Article:
    session = getSession()
    article = session.query(Article).filter(Article.url == url).first()
    return article

# Get All Articles for Pattern Id
def query_articles_by_pattern_id(pattern_id: str) -> List[Article]:
    session = getSession()
    pattern_matches = session.query(ArticlePatternMatch).filter(ArticlePatternMatch.pattern_id == pattern_id).all()
    article_ids = [pattern_match.article_id for pattern_match in pattern_matches]
    articles = session.query(Article).filter(Article.id.in_(article_ids)).all()
    return list(articles)

# Get All Articles where has_match is True
def query_articles_has_match(has_match: bool) -> List[Article]:
    session = getSession()
    articles = session.query(Article).filter(Article.has_match == has_match).all()
    return list(articles)

# Create Article and save to DB
def save_articles(articles: List[Article]):
    session = getSession()
    [session.add(article) for article in articles]
    session.commit()

# Create Article and save to DB
def save_article(article: Article):
    session = getSession()
    session.add(article)
    session.commit()
    
# Delete Article by Id
def delete_article(id: str):
    session = getSession()
    article = session.query(Article).filter(Article.id == id).first()
    session.delete(article)
    session.commit()
    session.close()
    
def update_article(article: Article):
    session = Session()
    session.query(Article).filter(Article.id == article.id).update({
        Article.title: article.title,
        Article.url: article.url,
        Article.date: article.date,
        Article.has_match: article.has_match,
        Article.news_source_id: article.news_source_id,
    })
    session.commit()
    session.close()


## News Source Queries

# Save News Source
def save_news_source(news_source: NewsSource):
    session = getSession()
    session.add(news_source)
    session.commit()

# Get All News Sources
def query_news_sources() -> List[NewsSource]:
    session = getSession()
    news_sources = session.query(NewsSource).all()
    return list(news_sources)

# Get News Source by Id
def query_news_source(id) -> NewsSource:
    session = getSession()
    news_source = session.query(NewsSource).filter(NewsSource.id == id).first()
    return news_source
    
# Update News Source
def update_news_source(news_source: NewsSource):
    session = getSession()
    session.query(NewsSource).filter(NewsSource.id == news_source.id).\
        update({
            NewsSource.url: news_source.url, 
            NewsSource.last_processed: news_source.last_processed, 
            NewsSource.status: news_source.status.value})
    session.commit()

# Delete News Source
def delete_news_source(id: str):
    session = getSession()
    news_source = session.query(NewsSource).filter(NewsSource.id == id).first()
    session.delete(news_source)
    session.commit()

## Pattern Queries

# Create Pattern
def save_pattern(pattern: Pattern):
    session = getSession()
    session.add(pattern)
    session.commit()

# Get All Patterns
def query_patterns() -> List[Pattern]:
    session = getSession()
    patterns = session.query(Pattern).all()
    return list(patterns)

# Get Pattern by Id
def query_pattern(id: str) -> Pattern:
    session = getSession()
    pattern = session.query(Pattern).filter(Pattern.id == id).first()
    return pattern

# Get All Patterns for Article Id
def query_patterns_matched_by_article(article_id: str) -> List[Pattern]:
    session = getSession()
    pattern_matches = session.query(ArticlePatternMatch).filter(ArticlePatternMatch.article_id == article_id).all()
    pattern_ids = [pattern_match.pattern_id for pattern_match in pattern_matches]
    patterns = session.query(Pattern).filter(Pattern.id.in_(pattern_ids)).all()
    return list(patterns)
    
# Update Pattern
def update_pattern(pattern: Pattern):
    session = getSession()
    session.query(Pattern).filter(Pattern.id == pattern.id).update({
        Pattern.regex: pattern.regex, 
    })
    session.commit()
    
# Delete Pattern
def delete_pattern(id: str):
    session = getSession()
    pattern = session.query(Pattern).filter(Pattern.id == id).first()
    session.delete(pattern)
    session.commit()
    
# Article Pattern Match Queries

# Create Article Pattern Match
def save_article_pattern_match(article_pattern_match: ArticlePatternMatch):
    session = getSession()
    session.add(article_pattern_match)
    session.commit()

def save_article_with_match(article: Article, pattern: Pattern):
    session = getSession()
    session.add(article)
    session.add(ArticlePatternMatch(article_id=article.id, pattern_id=pattern.id))
    session.commit()
