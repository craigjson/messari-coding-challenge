from sqlalchemy import Column, String
from data.postgres import Base

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
