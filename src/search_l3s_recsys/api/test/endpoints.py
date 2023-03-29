from http import HTTPStatus

# import flask
from flask import request, url_for

# import flask-restx
from flask_restx import Namespace, Resource, fields
from flask_restx.reqparse import RequestParser

# from search_l3s_recsys.api.test import ns_test

ns_test = Namespace("test", validate=True)

@ns_test.route("/recsys-test", endpoint="recsys-test")
class RecsysTest(Resource):
    def get(self):
        return {"message": "Success."}