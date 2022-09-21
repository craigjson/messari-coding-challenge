from typing import List

from data.models.pattern import Pattern
from data.query import (delete_pattern, query_pattern, query_patterns,
                        query_patterns_matched_by_article, save_pattern,
                        update_article, update_pattern)
from etl.pattern_match import article_content_matches_pattern

from api.article import query_articles_has_match


## Create Pattern
def create_pattern(pattern_id: str, pattern: str):
    save_pattern(pattern_id, pattern)
    # After we save a new pattern, we need to check if any articles match it
    articles_with_no_match = query_articles_has_match(has_match=False)
    for article in articles_with_no_match:
        if article_content_matches_pattern(article.content, pattern):
            article.has_match = True
            update_article(article)

## Get All Patterns
def get_patterns() -> List[Pattern]:
    return query_patterns()

## Get Pattern by Id
def get_pattern(pattern_id: str) -> Pattern:
    return query_pattern(pattern_id)

# Get Patterns by Article Id
def get_patterns_for_article_id(article_id: str) -> List[Pattern]:
    return query_patterns_matched_by_article(article_id)
    
## Update Pattern by Id
def update_pattern_by_id(pattern_id: str, pattern: str):
    update_pattern(pattern_id, pattern)
    # After we update a pattern, retrieve all articles that
    # 1. have no matches
    # 2. have a match with the pattern we just updated
    # 3. determine if the article still matches the pattern
    # 4. update the article's has_match field appropriately
    
## Delete Pattern by Id
def delete_pattern_by_id(pattern_id: str):
    delete_pattern(pattern_id)  
