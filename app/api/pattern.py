from turtle import update
from data.mock_data import patterns
from data.models import Pattern
from data.query import query_patterns, query_pattern, save_pattern, update_pattern, delete_pattern
from typing import List, Pattern as RegexPattern

## Create Pattern
def create_pattern(pattern_id: str, pattern: str):
    save_pattern(pattern_id, pattern)

## Get All Patterns
def get_patterns() -> List[Pattern]:
    return query_patterns()

## Get Pattern by Id
def get_pattern(pattern_id: str) -> Pattern:
    return query_pattern(pattern_id)
    
## Update Pattern by Id
def update_pattern_by_id(pattern_id: str, pattern: str):
    update_pattern(pattern_id, pattern)
    
## Delete Pattern by Id
def delete_pattern_by_id(pattern_id: str):
    delete_pattern(pattern_id)  