from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from data.postgres import Base

class Article(Base):
    __tablename__ = 'Article'
    
    id = Column(String, primary_key=True)
    source_id = Column(String, ForeignKey('Source.id'))
    title =  Column(String)
    content = Column(String)
    published = Column(DateTime)
    last_updated = Column(DateTime)
    patterns = relationship("Pattern", secondary="ArticlePatternMatch", backref="Article")
        
    def __repr__(self):
        return f"Article(id={self.id}, source_id={self.source_id} title={self.title}, content={self.content}, published={self.published}, last_updated={self.last_updated})"
            
    def __to_json__(self):
        return {
            'id': self.id,
            'source_id': self.source_id,
            'title': self.title,
            'content': self.content,
            'published': str(self.published),
            'last_updated': str(self.last_updated)
        }