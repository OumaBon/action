from flask import Flask
from flask_bootstrap import Bootstrap

style = Bootstrap()




def create_app():
    app = Flask(__name__)
    style.init_app(app)
    from app.api_v1 import api
    app.register_blueprint(api)
    return app