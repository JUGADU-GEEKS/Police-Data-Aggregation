from flask import Flask
from app import enterData 
from nonaggregated import search
from aggregated import aisearch
from home import home  # Import the home blueprint


def create_app():
    app = Flask(__name__)
    
    # Register the blueprint
    app.register_blueprint(enterData, url_prefix='/enterData')
    app.register_blueprint(search, url_prefix='/search')
    app.register_blueprint(aisearch, url_prefix='/aisearch')
    app.register_blueprint(home, url_prefix='/')  # Register the home blueprint

    
    return app
