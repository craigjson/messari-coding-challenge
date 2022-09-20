from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship

from util.crawl import CrawlStatus
from ..postgres import Base
class NewsSource(Base):
    __tablename__ = 'Source'

    id = Column(String, primary_key=True)
    url = Column(String)
    last_processed = Column(DateTime)
    status = Column(Integer)
    articles = relationship("Article", cascade="all, delete",)
        
    def __repr__(self):
        return f"NewsSource(id={self.id}, url={self.url}, last_processed={self.last_processed}, status={CrawlStatus(self.status).name})"
        
    def __to_json__(self):
        return {
            'id': self.id,
            'url': self.url,
            'last_processed': self.last_processed,
            'status': CrawlStatus(self.status).name
        }