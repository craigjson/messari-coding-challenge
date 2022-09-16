from typing import List

class Pattern:
    def __init__(self, pattern_id: str, pattern: str):
        self.id = pattern_id
        self.pattern = pattern
        
    def __repr__(self):
        return f"Pattern(id={self.id}, pattern={self.pattern})"
    
    def __to_json__(self):
        return {
            "id": self.id,
            "pattern": self.pattern
        }

class NewsSource:
    def __init__(self, id: str, url: str, patterns: List[str]=None):
        self.id = id
        self.url = url
        self.patterns = patterns
        
    def __repr__(self):
        return f"Feed(id={self.id}, url={self.url}, patterns={self.patterns})"
    
    def __to_json__(self):
        return {
            "id": self.id,
            "url": self.url,
            "patterns": self.patterns
        }
        
        
