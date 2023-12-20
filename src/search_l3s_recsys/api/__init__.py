"""API blueprint configuration"""
from flask import Blueprint
from flask_restx import Api
import sys

# sys.path.append("..")



api_bp = Blueprint("api", __name__, url_prefix="/l3s-recsys")
# authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}


api = Api(api_bp,
          version="0.0.2",
          title="L3S Recommendation Service for SEARCH",
          description="Welcome to the Swagger UI documentation site!",
        #   doc="/ui",
        #   authorizations=authorizations,
          )


from search_l3s_recsys.api.test.endpoints import ns_test
from search_l3s_recsys.api.random.endpoints import ns_random
from search_l3s_recsys.api.trends.endpoints import ns_trends

api.add_namespace(ns_test, path="/recsys-test")
api.add_namespace(ns_random, path="/random")
api.add_namespace(ns_trends, path="/trends")


