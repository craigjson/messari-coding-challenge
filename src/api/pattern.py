from ..data.data import patterns
from ..models.models import Pattern
from typing import List, Pattern as RegexPattern

## Create Pattern
def create_pattern(pattern_id: str, pattern: RegexPattern):
    patterns.append(Pattern(
        pattern_id = pattern_id,
        pattern = pattern
    ))

## Get All Patterns
def get_patterns():
    return patterns

## Get Pattern by Id
def get_pattern(pattern_id: str):
    return patterns[pattern_id]

## Update Pattern by Id
def update_pattern(pattern_id: str, pattern: RegexPattern):
    pattern = patterns[pattern_id]
    pattern.pattern = pattern

## Delete Pattern by Id
def delete_pattern(pattern_id: str):
    del patterns[pattern_id]    