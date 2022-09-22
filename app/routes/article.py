from api.article import get_all_articles, get_article_by_id, get_articles_for_pattern
from etl.run_feed import extract_transform_load_feed
from flask import Blueprint, jsonify, request

app_article = Blueprint("articles_app", __name__)

## Article Routes

## Get All Articles
@app_article.route("/articles", methods=["GET"])
def get_articles_route():
    try:
        return [article.__to_json__() for article in get_all_articles()]
    except Exception as e:
        return jsonify({"error": f"Error getting articles \nError: {e}"}), 400
    
## Get Articles by Article Id
@app_article.route("/article/<string:article_id>", methods=["GET"])
def get_article_route(article_id: str):
    try:
        article = get_article_by_id(article_id)
        if article:
            return jsonify(article.__to_json__())
        raise Exception(f"Article: {article_id} not found")
    except Exception as e:
        return jsonify({"error": f"Error getting articles for news source {article_id} \nError: {e}"}), 400
    
## Get Articles by Article Id
@app_article.route("/articles/pattern/", methods=["GET"])
def get_articles_by_pattern_route():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "No input data provided"}), 400
    if not request_data["id"]:
        return jsonify({"error": "No pattern id provided"}), 400
    pattern_id = request_data["id"]
    try:
        return [article.__to_json__() for article in get_articles_for_pattern(pattern_id)]
    except Exception as e:
        return jsonify({"error": f"Error getting articles for pattern {pattern_id} \nError: {e}"}), 400
