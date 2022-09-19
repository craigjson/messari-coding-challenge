import json
from typing import List, Pattern as RegexPattern

class Article(dict):
    def __init__(self, id, title, content, published):
        dict.__init__(self, id=id, title=title, content=content, published=published)
             
class Pattern(dict):
    def __init__(self, id: str, pattern: RegexPattern):
        dict.__init__(self, id=id, pattern=pattern)

class NewsSource(dict):
    def __init__(self, id: str, url: str, patterns: List[str]=None):
        dict.__init__(self, id=id, url=url, patterns=patterns)