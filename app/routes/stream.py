from flask import jsonify, request
from flask_sse import ServerSentEventsBlueprint, sse

app_stream = ServerSentEventsBlueprint("stream_app", __name__)

# Stream Routes
@app_stream.route("/subscribe")
def subscribe_to_pattern_stream():
    channel = request.args.get("channel")
    if not channel:
        return jsonify({"error": "No channel provided for subscription"}), 400
    
    # Headers are temporary since I am developing locally and subscribing to the stream from 
    # a different port on the same machine. This will be removed when deployed to production.
    headers = {"Access-Control-Allow-Origin": "*", "content-type": "text/event-stream"}
    resp = sse.stream()
    resp.headers = headers
    return resp
