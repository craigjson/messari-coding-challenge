from re import search
from typing import List

from data.query import query_patterns


def article_content_matches_pattern(article_content: str) -> List[str]:
    patterns = query_patterns()
    for pattern in patterns:
        if search(pattern.pattern, article_content):
            return True
    return False
