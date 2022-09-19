from sqlalchemy import Column, String, Date
from .postgres import Base

from typing import List

class Article(Base):
    __tablename__ = 'Article'
    
    id = Column(String, primary_key=True)
    title =  Column(String)
    content = Column(String)
    published = Column(Date)
        
    def __repr__(self):
        return f"Article(id={self.id}, title={self.title}, content={self.content}, published={self.published})"
            
    def __to_json__(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'published': self.published
        }
        
class Pattern(Base):
    __tablename__ = 'Pattern'
    
    id = Column(String, primary_key=True)
    pattern = Column(String)
    
    def __repr__(self):
        return f"Pattern(id={self.id}, pattern={self.pattern})"
    
    def __to_json__(self):
        return {
            'id': self.id,
            'pattern': self.pattern
        }

class NewsSource(Base):
    __tablename__ = 'Source'

    id = Column(String, primary_key=True)
    url = Column(String)
    patterns = None
        
    def __repr__(self):
        return f"NewsSource(id={self.id}, url={self.url}, patterns={self.patterns})"

    def __to_json__(self):
        return {
            'id': self.id,
            'url': self.url,
            'patterns': self.patterns
        }