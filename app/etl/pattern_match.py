from re import search
from typing import List

from data.models.article import Article
from data.models.article_pattern_match import ArticlePatternMatch
from data.query import query_patterns, save_article_pattern_match


# Determine if an article matches a pattern, save the match to the database
def article_content_matches_pattern(article: Article) -> List[str]:
    patterns = query_patterns()
    for pattern in patterns:
        if search(pattern.pattern, article.content):
            # Save pattern match to DB
            save_article_pattern_match(ArticlePatternMatch(article_id=article.id, pattern_id=pattern.id))
            return True
    return False