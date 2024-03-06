from http import HTTPStatus
import os, requests

from werkzeug.exceptions import BadRequest
from requests.exceptions import InvalidURL

# import flask
from flask import request, url_for

# import flask-restx
from flask_restx import Namespace, Resource, fields
from flask_restx.reqparse import RequestParser

# from search_l3s_recsys.api.test import ns_test

## ------------------- config: sse_search_client ----------------- ##
from swagger_client import sse_search_client
sse_search_config = sse_search_client.Configuration()
sse_search_config.host = os.getenv('SSE_SEARCH_HOST')
print("*"*80)
print("sse-search-service-host: ", sse_search_config.host)
print("*"*80)

## ----------------- import api modules from sse client ----------------- ##
client_sse_search = sse_search_client.ApiClient(configuration=sse_search_config)
sse_skill_api = sse_search_client.SkillApi(api_client=client_sse_search)
sse_learningunit_api = sse_search_client.LearningUnitsApi(api_client=client_sse_search)
sse_learningpath_api = sse_search_client.LearningPathApi(api_client=client_sse_search)
sse_user_api = sse_search_client.UserApi(api_client=client_sse_search)

## ----------------- import dtos from sse_search_client ----------------- ##
from swagger_client.sse_search_client.models.skill_list_dto import SkillListDto
from swagger_client.sse_search_client.models.search_learning_unit_list_dto import SearchLearningUnitListDto


## registration - l3s gateway

## import dto
from .dto import test_model
ns_test = Namespace("Tests", validate=True, description="Tests for L3S Recsys Service")

## dto registration
ns_test.models[test_model.name] = test_model

@ns_test.route("/test", endpoint="recsys-test")
class RecsysTest(Resource):
    @ns_test.marshal_with(test_model)
    def get(self):
        return {"message": "success"}, HTTPStatus.OK
    
    @ns_test.expect(test_model)
    @ns_test.marshal_with(test_model)
    def post(self):
        msg = ns_test.payload
        return msg, HTTPStatus.CREATED

from .dto import dto_connection_response
ns_test.models[dto_connection_response.name] = dto_connection_response
    
@ns_test.route("/connection-sse", endpoint="recsys_connection_sse")
class RecsysTestConnectionSSE(Resource):
    @ns_test.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_test.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_test.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_test.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    @ns_test.marshal_with(dto_connection_response)
    def get(self):
        url = sse_search_config.host
        print(url)
        result = {}
        try:
            response = requests.head(url+"/api")
            if response.status_code == 200:
                result.update({"host_url": url, "status": 'success'})
                return result, HTTPStatus.OK
            else:
                result.update({"host_url": url, "status": 'failed'})
                return result, HTTPStatus.INTERNAL_SERVER_ERROR
        except requests.ConnectionError as e:
            result = {"host_url": url}
            result.update({"status": e.args[0]})
            return result, HTTPStatus.NOT_FOUND
        except InvalidURL as e:
            result = {"host_url": url}
            result.update({"status": e.args[0]})
            return result, HTTPStatus.BAD_REQUEST
        
