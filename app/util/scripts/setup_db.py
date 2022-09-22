from data.models.article import Article
from data.models.article_pattern_match import ArticlePatternMatch
from data.models.news_source import NewsSource
from data.models.pattern import Pattern
from data.postgres import Base, Session, engine
from sqlalchemy import inspect



def create_db_tables():
    session = Session()
    # check if DB Tables already exist
    if not inspect(engine).has_table("Source", schema="public"):
        try:
            Base.metadata.create_all(engine)
            print("created DB")
            session.commit()
        except Exception as e:
            print (f"Failed to create DB tables with error: {e}")
    session.close()