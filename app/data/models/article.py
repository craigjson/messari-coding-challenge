from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from ..postgres import Base

class Article(Base):
    __tablename__ = 'Article'
    
    id = Column(String, primary_key=True)
    source_id = Column(String, ForeignKey('Source.id'))
    title =  Column(String)
    content = Column(String)
    published = Column(DateTime)
    last_updated = Column(DateTime)
    has_match = Column(Boolean, default=False)
        
    def __repr__(self):
        return f"Article(id={self.id}, title={self.title}, content={self.content}, published={self.published}, last_updated={self.last_updated})"
            
    def __to_json__(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'published': self.published,
            'last_updated': self.last_updated
        }