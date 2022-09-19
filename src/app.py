from flask import Flask
from .routes.news_source import app_news_source
from .routes.pattern import app_pattern
from .routes.articles import app_articles

# Initalize Flask App
app = Flask(__name__)

# Hello World Route
@app.route("/")
def hello_world():
    return "<p>Messari Coding Challenge!</p>"

# Register Blueprints
app.register_blueprint(app_news_source)
app.register_blueprint(app_pattern)
app.register_blueprint(app_articles)