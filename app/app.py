from os import getenv

from dotenv import load_dotenv
from flask import Flask

from routes.article import app_article
from routes.news_source import app_news_source
from routes.pattern import app_pattern
from routes.stream import app_stream
from scripts.load_mock_data import load_mock_data

# Load Postgres Data
try:
    load_mock_data()
    print()
except Exception as e:
    print(e)
    
# Attempt to load .env file
load_dotenv()

# Initalize Flask App
app = Flask(__name__)
REDIS_HOST = getenv("REDIS_HOST")
REDIS_PORT = getenv("REDIS_PORT")
if REDIS_HOST and REDIS_PORT:
    app.config["REDIS_URL"] = f"redis://{REDIS_HOST}:{REDIS_PORT}"

# Hello World Route
@app.route("/")
def hello_world():
    return "<p>Messari Coding Challenge!</p>"

# Register Blueprints
app.register_blueprint(app_news_source)
app.register_blueprint(app_pattern)
app.register_blueprint(app_article)
app.register_blueprint(app_stream, url_prefix="/stream")