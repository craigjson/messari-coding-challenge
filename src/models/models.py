from typing import List, Pattern as RegexPattern

class Article:
    def __init__(self, id, title, content, published):
        self.id = id
        self.title = title
        self.content = content
        self.published = published
        
    def __repr__(self):
        return f"Article({self.id}, {self.title}, {self.content}, {self.published})"
    
    def to__json__(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "published": self.published
        }
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