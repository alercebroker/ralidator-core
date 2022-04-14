import pytest
from flask import Flask
from ralidator_flask.ralidator_flask import RalidatorFlask


@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    filters_map = {"test": "ok"}
    app.config["FILTERS_MAP"] = filters_map
    return app


@pytest.fixture
def ralidator_flask(app) -> RalidatorFlask:
    rf = RalidatorFlask()
    rf.init_app(app)
    return rf