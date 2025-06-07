from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec
from .api import register_routes
from .api import receipt_bp
from .api import test_bp


def create_app():
    app = Flask(__name__)

    api = FlaskPydanticSpec("flask", title="Fetch Backend Challenge")
    api.register(app)

    # routes init
    register_routes(api)

    # blueprint routes
    app.register_blueprint(receipt_bp)
    app.register_blueprint(test_bp)

    return app
