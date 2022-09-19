from flask import Blueprint, request, jsonify
from ..api.articles import get_all_articles, get_article_by_id

app_articles = Blueprint("articles_app", __name__)

## Article Routes

## Get All Articles
@app_articles.route("/articles", methods=["GET"])
def get_articles_route():
    try:
        return jsonify(get_all_articles())
    except Exception as e:
        return jsonify({"error": f"Error getting articles \nError: {e.message}"}), 400
    
## Get Articles by Article Id
@app_articles.route("/articles/<string:article_id>", methods=["GET"])
def get_article_route(article_id: str):
    try:
        return jsonify(get_article_by_id(article_id))
    except Exception as e:
        return jsonify({"error": f"Error getting articles for news source {article_id} \nError: {e.message}"}), 400