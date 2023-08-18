"""API blueprint configuration"""
from flask import Blueprint
from flask_restx import Api



api_bp = Blueprint("api", __name__, url_prefix="/l3s-recsys")
# authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}


api = Api(api_bp,
          version="0.0.1",
          title="L3S Recommendation Service for SEARCH",
          description="Welcome to the Swagger UI documentation site!",
        #   doc="/ui",
        #   authorizations=authorizations,
          )


from search_l3s_recsys.api.test.endpoints import ns_test
api.add_namespace(ns_test, path="/recsys-test")

