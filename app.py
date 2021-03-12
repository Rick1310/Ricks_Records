"""Here we will hold all the routing for the app"""

from flask import Flask, render_template
from .models import DB, Migrate
from os import getenv


def create_app():
    """Creation and configuration of an instance of the flask application"""
    app = Flask(__name__)
    
    # database and app configs
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    #Initialize DB
    DB.init_app(app)
    Migrate.init_app(app, DB)
    
    
    """Here we have decorators to listen for specific endpoint visits"""
    
    @app.route('/')
    def home():
        """Landing Page"""
        return render_template(
            'home.html',
            title="Home",
            description="Landing Page"
        )
    
    @app.route('/About', methods=["GET"])
    def about():
        return render_template('about.html', title="About")
    
    @app.route('Collection', methods =["get"])
    def collection():
        return render_template()
    
    
    
    
    



