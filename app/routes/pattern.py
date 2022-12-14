from flask import Blueprint, request, jsonify
from api.pattern import create_pattern, get_patterns, get_pattern, update_pattern_by_id, delete_pattern, get_patterns_for_article_id

app_pattern = Blueprint("pattern_app", __name__)

## Create Pattern
@app_pattern.route("/pattern/create/", methods=["POST"])
def save_pattern():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "No input data provided"}), 400
    if not request_data["id"]:
        return jsonify({"error": "No pattern id provided"}), 400
    if not request_data["pattern"]:
        return jsonify({"error": "No pattern provided"}), 400

    try:
        create_pattern(request_data["id"], request_data["pattern"])
        return jsonify({"message": "Pattern created successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Pattern creation failed \nError: {e}"}), 400

## Get All Patterns
@app_pattern.route("/patterns")
def get_patterns_route():
    try:
        return jsonify([pattern.__to_json__() for pattern in get_patterns()])
    except Exception as e:
        return jsonify({"error": f"Error getting patterns \nError: {e}"}), 400

## Get Pattern by Id
@app_pattern.route("/pattern/<string:pattern_id>")
def get_pattern_route(pattern_id: str):
    try:
        pattern = get_pattern(pattern_id)
        if pattern:
            return jsonify(pattern.__to_json__())
        raise Exception(f"Article: {pattern_id} not found")
    except Exception as e:
        return jsonify({"error": f"Error getting pattern {pattern_id} \nError: {e}"}), 400

## Get Patterns by Article Id
@app_pattern.route("/patterns/article/", methods=["GET"])
def get_patterns_by_article_route():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "No input data provided"}), 400
    if not request_data["id"]:
        return jsonify({"error": "No pattern id provided"}), 400
    article_id = request_data["id"]
    try:
        return [pattern.__to_json__() for pattern in get_patterns_for_article_id(article_id)]
    except Exception as e:
        return jsonify({"error": f"Error getting patterns for article {article_id} \nError: {e}"}), 400

## Update Pattern by Id
@app_pattern.route("/pattern/update/", methods=["POST"])
def update_pattern_route():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "No input data provided"}), 400
    if not request_data["id"]:
        return jsonify({"error": "No pattern id provided"}), 400
    if not request_data["pattern"]:
        return jsonify({"error": "No pattern provided"}), 400
    
    try:
        update_pattern_by_id(request_data["id"], request_data["pattern"])
        return jsonify({"message": "Pattern updated successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Pattern update failed \nError: {e}"}), 400

## Delete Pattern by Id
@app_pattern.route("/pattern/delete/")
def delete_pattern_route():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "No input data provided"}), 400
    if not request_data["id"]:
        return jsonify({"error": "No source id provided"}), 400
    
    try:
        delete_pattern(request_data["id"])
        return jsonify({"message": "Pattern deleted successfully"}), 201
    except Exception as e:
        return jsonify({"error": "Pattern deletion failed \nError: {e.message}"}), 400