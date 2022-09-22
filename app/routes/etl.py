from etl.run_feed import extract_transform_load_feed
from flask import Blueprint, jsonify

app_etl = Blueprint("etl_app", __name__)

# Run ETL Feed
@app_etl.route("/feed/run_etl", methods=["GET"])
def run_etl():
    try:
        extract_transform_load_feed()
        return jsonify({"message": "ETL Feed ran successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Error running ETL Feed \nError: {e}"}), 400