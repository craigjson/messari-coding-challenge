from typing import List
from .models import Article, NewsSource, Pattern
from .postgres import Session


## Article Queries

# Get All Articles
def query_articles() -> List[Article]:
    session = Session()
    articles = session.query(Article).all()
    session.close() 
    return list(articles)

# Get Article by Id
def query_artcile(id) -> Article:
    session = Session()
    article = session.query(Article).filter(Article.id == id).first()
    session.close() 
    return article

# Get Article by Title
def query_article_by_title(title) -> Article:
    session = Session()
    article = session.query(Article).filter(Article.title == title).first()
    session.close()
    return article

# Create Article and save to DB
def save_article(id, title, content, published):
    session = Session()
    article = Article(
        id = id,
        title = title,
        content = content,
        published = published
    )
    session.add(article)
    session.commit()
    session.close()

## News Source Queries

# Save News Source
def save_news_source(source_id: str, url: str, patterns=None):
    session = Session()
    news_source = NewsSource(
        id = source_id,
        url = url,
        patterns = patterns
    )
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
def update_news_source(id, url, patterns):
    session = Session()
    news_source = session.query(NewsSource).filter(NewsSource.id == id).first()
    news_source.url = url
    news_source.patterns = patterns
    session.update(news_source)
    session.commit()
    session.close()
    return news_source

# Delete News Source
def delete_news_source(id):
    session = Session()
    news_source = session.query(NewsSource).filter(NewsSource.id == id).first()
    session.delete(news_source)
    session.commit()
    session.close()

## Pattern Queries

# Create Pattern
def save_pattern(id, name, regex, news_source_id):
    session = Session()
    pattern = Pattern(
        id = id,
        name = name,
        regex = regex,
        news_source_id = news_source_id
    )
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
def query_pattern(id) -> Pattern:
    session = Session()
    pattern = session.query(Pattern).filter(Pattern.id == id).first()
    session.close()
    return pattern

# Update Pattern
def update_pattern(id, name, regex, news_source_id):
    session = Session()
    pattern = session.query(Pattern).filter(Pattern.id == id).first()
    pattern.name = name
    pattern.regex = regex
    pattern.news_source_id = news_source_id
    session.update(pattern)
    session.commit()
    session.close()
    return pattern

# Delete Pattern
def delete_pattern(id):
    session = Session()
    pattern = session.query(Pattern).filter(Pattern.id == id).first()
    session.delete(pattern)
    session.commit()
    session.close()