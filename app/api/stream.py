from data.models.article import Article
from data.models.pattern import Pattern
from flask_sse import sse


# Publish an article to the appropriate streams
def publish_article_to_stream(article: Article, pattern: Pattern):
    # Publish article to stream for pattern
    sse.publish(format_stream_data(article), channel=pattern.id)
    # Publish the article to the news source channel
    sse.publish(format_stream_data(article), channel=article.source_id)
    
# Format the article data for the stream
def format_stream_data(article: Article):
    return f"""data: \nTitle: {article.title}\nContent: {article.content}\nPublished: {article.published}\nLink: {article.id}\n\n"""
