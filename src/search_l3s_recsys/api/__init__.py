"""API blueprint configuration"""
from flask import Blueprint
from flask_restx import Api
import sys

# sys.path.append("..")



api_bp = Blueprint("api", __name__, url_prefix="/l3s-recsys")
# authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}


api = Api(api_bp,
          version="0.0.3",
          title="L3S Recommendation Service for SEARCH",
          description="Welcome to the Swagger UI documentation site!",
        #   doc="/ui",
        #   authorizations=authorizations,
          )


from search_l3s_recsys.api.test.endpoints import ns_test
from search_l3s_recsys.api.random.endpoints import ns_random
from search_l3s_recsys.api.trends.endpoints import ns_trends
from search_l3s_recsys.api.digitalisation_topics.endpoints import ns_digi_topics
from search_l3s_recsys.api.learning_goals.endpoints import ns_learning_goals_rec
from search_l3s_recsys.api.interests.endpoints import ns_interests_rec

api.add_namespace(ns_test, path="/recsys")
api.add_namespace(ns_random, path="/recsys")
api.add_namespace(ns_trends, path="/recsys")
api.add_namespace(ns_digi_topics, path="/recsys")
api.add_namespace(ns_learning_goals_rec, path="/recsys")
api.add_namespace(ns_interests_rec, path="/recsys")


