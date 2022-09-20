from sqlalchemy import Column, String
from ..postgres import Base

from typing import List

class NewsSource(Base):
    __tablename__ = 'Source'

    id = Column(String, primary_key=True)
    url = Column(String)
            
    def __repr__(self):
        return f"NewsSource(id={self.id}, url={self.url})"

    def __to_json__(self):
        return {
            'id': self.id,
            'url': self.url,
        }