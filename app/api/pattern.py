from typing import List

from data.models.pattern import Pattern
from data.query import (delete_pattern, query_pattern, query_patterns,
                        query_patterns_matched_by_article, save_pattern)
from etl.pattern_match import article_content_matches_pattern

from api.article import get_all_articles


## Create Pattern
def create_pattern(pattern_id: str, pattern: str):
    pattern = Pattern(id=pattern_id, pattern=pattern)
    save_pattern(pattern)
    # After we save a new pattern, re-process articles with new pattern
    articles = get_all_articles()
    for article in articles:
        try:
            article_content_matches_pattern(article, pattern)
        except Exception as e:
            print(f"Error matching pattern {pattern_id} to article {article.id}: {e}")

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
## Implement as a delete and create to keep things simple even though it's not efficient
def update_pattern_by_id(pattern_id: str, pattern: str):
    delete_pattern_by_id(pattern_id)
    create_pattern(pattern_id, pattern)
        
## Delete Pattern by Id
## Will also delete all Article Pattern Matches via cascade
def delete_pattern_by_id(pattern_id: str):
    delete_pattern(pattern_id)
