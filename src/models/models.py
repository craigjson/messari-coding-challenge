from typing import List, Pattern as RegexPattern

class Pattern:
    def __init__(self, id: str, pattern: RegexPattern):
        self.id = id
        self.pattern = pattern
        
    def __repr__(self):
        return f"Pattern(id={self.id}, pattern={self.pattern.pattern})"
    
    def __to_json__(self):
        return {
            "id": self.id,
            "pattern": self.pattern.pattern
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