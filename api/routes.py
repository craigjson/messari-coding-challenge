from flask import Flask, request, jsonify
from api.api import delete_pattern
from api import save_news_source, get_source, get_sources, update_source, delete_source, create_pattern, get_patterns, get_pattern, update_pattern

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

### News Source Routes

## Create News Source
@app.route("/source/create/", methods=["POST"])
def save_news_source():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "No input data provided"}), 400
    if not request_data["id"]:
        return jsonify({"error": "No source id provided"}), 400
    if not request_data["url"]:
        return jsonify({"error": "No source url provided"}), 400
    
    save_news_source(request_data["id"], request_data["url"], request_data["patterns"])
    return jsonify({"message": "Source created successfully"}), 201

## Get NewsSource by Id
@app.route("/source/<string:id>")
def get_source_route(id):
    return get_source(id)
    
## Get All NewsSources
@app.route("/sources")
def get_sources_route():
    return get_sources()

## Update NewsSource
@app.route("/source/update/", methods=["PUT"])
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
@app.route("/source/delete/<string:id>")
def delete_source_route(id):
    delete_source(id)
    return jsonify({"message": "Source deleted successfully"}), 201



### Pattern Routes

## Create Pattern
@app.route("/pattern/save/", methods=["POST"])
def save_pattern():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "No input data provided"}), 400
    if not request_data["id"]:
        return jsonify({"error": "No pattern id provided"}), 400
    if not request_data["pattern"]:
        return jsonify({"error": "No pattern provided"}), 400

    create_pattern(request_data["id"], request_data["pattern"])
    return jsonify({"message": "Pattern created successfully"}), 201

## Get All Patterns
@app.route("/patterns")
def get_patterns_route():
    return get_patterns()

## Get Pattern by Id
@app.route("/pattern/<string:pattern_id>")
def get_pattern_route(pattern_id):
    return get_pattern(pattern_id)

## Update Pattern by Id
@app.route("/pattern/update/", methods=["PUT"])
def update_pattern_route():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "No input data provided"}), 400
    if not request_data["id"]:
        return jsonify({"error": "No pattern id provided"}), 400
    if not request_data["pattern"]:
        return jsonify({"error": "No pattern provided"}), 400
    
    update_pattern(request_data["id"], request_data["pattern"])
    
    return jsonify({"message": "Pattern updated successfully"}), 201

## Delete Pattern by Id
@app.route("/pattern/delete/<string:pattern_id>")
def delete_pattern_route(pattern_id):
    delete_pattern(pattern_id)
    return jsonify({"message": "Pattern deleted successfully"}), 201
    