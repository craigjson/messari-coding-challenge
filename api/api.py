from flask import Flask, jsonify
from data import sources, patterns
from models import NewsSource, Pattern
from typing import List

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


### News Source Routes

## Create News Source
def save_news_source(id, url, patterns):
    sources.append(NewsSource(
        id = id,
        url = url,
        patterns = patterns
    ))

## Get NewsSource by Id
def get_source(id):
   return sources[id].__to_json__()
    
## Get All NewsSources
def get_sources():
   return [f"<p>{source.__to_json__()}</p>" for source in sources]

## Update NewsSource
def update_source(id, url, patterns):
    source = sources[id]
    source.url = url
    source.patterns = patterns

## Delete NewsSource
def delete_source(id):
    del sources[id]
    return f"Source {id} deleted"

### Pattern Routes

## Create Pattern
def create_pattern(pattern_id: str, pattern: List[str]):
    patterns.append(Pattern(
        pattern_id = pattern_id,
        pattern = pattern
    ))

## Get All Patterns
def get_patterns():
    return [f"<p>{pattern.__to_json__()}</p>" for pattern in patterns]

## Get Pattern by Id
def get_pattern(pattern_id):
    return patterns[pattern_id].__to_json__()

## Update Pattern by Id
def update_pattern(pattern_id, pattern):
    pattern = patterns[pattern_id]
    pattern.pattern = pattern

## Delete Pattern by Id
def delete_pattern(pattern_id):
    del patterns[pattern_id]    