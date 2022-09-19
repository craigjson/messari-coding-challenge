from flask import Blueprint, request, jsonify
from api.news_source import save_news_source, get_source, get_sources, update_source, delete_source

app_news_source = Blueprint("news_source_app", __name__)

## Create News Source
@app_news_source.route("/source/create/", methods=["POST"])
def save_news_source():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "No input data provided"}), 400
    if not request_data["id"]:
        return jsonify({"error": "No source id provided"}), 400
    if not request_data["url"]:
        return jsonify({"error": "No source url provided"}), 400
    
    try:
        save_news_source(request_data["id"], request_data["url"], request_data["patterns"])
        return jsonify({"message": "Source created successfully"}), 201
    except Exception as e:
        return jsonify({"error": "Error creating source \nError: {e.message}"}), 400

## Get NewsSource by Id
@app_news_source.route("/source/<string:source_id>")
def get_source_route(source_id: str):
    try:
        return get_source(source_id)
    except Exception as e:
        return jsonify({"error": f"Error getting source {source_id} \nError: {e.message}"}), 400
    
## Get All NewsSources
@app_news_source.route("/sources")
def get_sources_route():
    try:
        return get_sources()
    except Exception as e:
        return jsonify({"error": "Error getting sources \nError: {e.message}"}), 400

## Update NewsSource
@app_news_source.route("/source/update/", methods=["PUT"])
def update_source():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "No input data provided"}), 400
    if not request_data["id"]:
        return jsonify({"error": "No source id provided"}), 400
    if not request_data["url"]:
        return jsonify({"error": "No source url provided"}), 400
    
    update_source(request_data["id"], request_data["url"], request_data["patterns"])
    return jsonify({"message": "Source updated successfully"}), 201

## Delete NewsSource
@app_news_source.route("/source/delete/")
def delete_source_route():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "No input data provided"}), 400
    if not request_data["source_id"]:
        return jsonify({"error": "No source id provided"}), 400
    
    try:
        delete_source(request_data["source_id"])
        return jsonify({"message": "Source deleted successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Source deletion failed \nError: {e.message}"}), 400

