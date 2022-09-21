from flask import Flask
from routes.news_source import app_news_source
from routes.pattern import app_pattern
from routes.article import app_article

from scripts.load_mock_data import load_mock_data
from dotenv import load_dotenv

# Load Postgres Data
try:
    #load_mock_data()
    print()
except Exception as e:
    print(e)
    
# Attempt to load .env file
load_dotenv()

# Initalize Flask App
app = Flask(__name__)

# Hello World Route
@app.route("/")
def hello_world():
    return "<p>Messari Coding Challenge!</p>"

# Register Blueprints
app.register_blueprint(app_news_source)
app.register_blueprint(app_pattern)
app.register_blueprint(app_article)