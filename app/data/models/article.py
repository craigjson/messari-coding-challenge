from sqlalchemy import Column, String, Date
from ..postgres import Base

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