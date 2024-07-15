from fastapi_pagination import Page, pagination_params
from fastapi import Depends, FastAPI

def add_pagination(app: FastAPI):
    app.dependency_overrides[pagination_params] = pagination_params
