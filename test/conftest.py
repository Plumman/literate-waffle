import pytest 

# from literate-waffle.phasebook import create_app
import importlib

module_name = 'phasebook'
module = importlib.import_module(module_name)


@pytest.fixture()
def app():
    app = module.create_app()
    yield app 

@pytest.fixture()
def client(app):
   return app.test_client()