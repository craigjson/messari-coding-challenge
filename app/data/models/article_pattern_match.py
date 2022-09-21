from sqlalchemy import Column, String, ForeignKey, Table
from ..postgres import Base

ArticlePatternMatch = Table(
    'ArticlePatternMatch', Base.metadata,
    Column('article_id', String, ForeignKey('Article.id')),
    Column('pattern_id', String, ForeignKey('Pattern.id'))
)