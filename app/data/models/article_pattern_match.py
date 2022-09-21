from sqlalchemy import Column, String, ForeignKey, Table
from ..postgres import Base

class ArticlePatternMatch(Base):
    __tablename__ = 'ArticlePatternMatch'
    article_id = Column(String, ForeignKey('Article.id'), primary_key=True)
    pattern_id = Column(String, ForeignKey('Pattern.id'), primary_key=True)