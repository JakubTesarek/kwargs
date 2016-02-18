import pytest
from kwargs.kwargs import App

def test_can_create_app():
    app = App()
    assert isinstance(app, App)