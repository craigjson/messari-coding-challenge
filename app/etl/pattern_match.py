from re import search
from typing import List

from api.pattern import get_patterns


def article_content_matches_pattern(article_content: str) -> List[str]:
    patterns = get_patterns()
    for pattern in patterns:
        if search(pattern.pattern, article_content):
            return True
    return False
