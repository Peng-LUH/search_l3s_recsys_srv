from http import HTTPStatus
import os, json
from pprint import pprint
import random
from dotenv import load_dotenv
load_dotenv()

# import flask
from flask import request, url_for

# import flask-restx
from flask_restx import Namespace, Resource, fields
from flask_restx import reqparse

## import dto
from .dto import dto_random_response

ns_random = Namespace("Random Recommendation", validate=True)

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
from swagger_client.sse_search_client.models.search_learning_unit_dto import SearchLearningUnitDto
from swagger_client.sse_search_client.models.learning_path_list_dto import LearningPathListDto

# ## dto registration
# ns_random.models[dto_random_response.name] = dto_random_response
# # request input parser
# parser_random_recs = reqparse.RequestParser()
# parser_random_recs.add_argument('num_of_recs', type=int, required=True, location='args', default=10)

# @ns_random.route("/get-random-recommendation", endpoint="random")
# class RandomRecommendation(Resource):
#     @ns_random.response(int(HTTPStatus.CREATED), "Success")
#     @ns_random.response(int(HTTPStatus.BAD_REQUEST), "Number of recommendation is either negative or exceed the number of existing contents")
#     @ns_random.expect(parser_random_recs)
#     @ns_random.marshal_with(dto_random_response)
#     def get(self):
#         request_data = parser_random_recs.parse_args()
#         num_of_rec = request_data.get("num_of_rec")
        
#         # print(os.environ["BASE_DATASETS_PATH"])
#         json_file_dir = os.path.join(os.getenv('BASE_DATASETS_PATH'), 'mls-tasks-full/json/data.json')
#         print(json_file_dir)
#         with open(json_file_dir) as f:
#             data_arr = json.load(f)

#         len_of_data = len(data_arr)
        
#         try: 
#             if num_of_rec > len_of_data:
#                 raise ValueError("Number of recommendation requested cannot be larger than the number of contents existing.")

#             if num_of_rec < 0:
#                 raise ValueError("Number of recommendation cannot be negativ")
            
#             random_elements = random.sample(data_arr, num_of_rec)
#             print(type(random_elements))
#             ids = []
#             for e in random_elements:
#                 print(e['@id'])
#                 ids.append(e["@id"])
            
#             print(type(ids))
#             response = {"results": ids}
            
#             return response, HTTPStatus.CREATED
        
#         except ValueError as e:
#             return e.args, HTTPStatus.BAD_REQUEST
#         except TypeError as e:
#             return e.args, HTTPStatus.CONFLICT
        



parser_random = reqparse.RequestParser()
parser_random.add_argument('num_of_recs', type=int, location='args', default=10, required=True)
parser_random.add_argument('orga_ids', type=str, action='append', location='args', default=None)

from .dto import dto_random_response
ns_random.models[dto_random_response.name] = dto_random_response

## --------------------- get random skill ------------------- ##
@ns_random.route("/get-random-skill", endpoint="get_random_skill")
class GetRandomSkill(Resource):
    @ns_random.expect(parser_random)
    @ns_random.marshal_with(dto_random_response)
    def get(self):
        try:
            # get request data
            request_data = parser_random.parse_args()
            num_of_recs = request_data['num_of_recs']
            
            # get list of skills
            response = sse_skill_api.skill_mgmt_controller_get_all_skills()
            d = SkillListDto(skills=response.skills)
            request_data = d.to_dict()        
            list_of_skills = request_data["skills"]
            
            skill_ids = [d["id"] for d in list_of_skills]
            max_num = len(skill_ids)

            message = "success"
            data_type = "skill"
            
            if num_of_recs < max_num:
                results = random.sample(skill_ids, num_of_recs)
            else:
                message = f"Max number of results reached: Requires {num_of_recs} results, {max_num} returned."
                results = skill_ids
                
            return {"message": message, "type": data_type, "results": results}, HTTPStatus.OK
        
        except ValueError as e:
            return e.args, HTTPStatus.BAD_REQUEST
        except TypeError as e:
            return e.args, HTTPStatus.CONFLICT

## ----------------- get random tasks ------------------ ##
@ns_random.route("/get-random-tasks", endpoint="get_random_tasks")
class GetRandomTasks(Resource):
    @ns_random.expect(parser_random)
    @ns_random.marshal_with(dto_random_response)
    def get(self):
        try:
            # get request data
            request_data = parser_random.parse_args()
            num_of_recs = request_data['num_of_recs']
            orga_ids = request_data['orga_ids']
            
            response = sse_learningunit_api.search_learning_unit_controller_list_learning_units()
            d = SearchLearningUnitListDto(learning_units=response.learning_units)
            request_data = d.to_dict()
            list_of_tasks = request_data["learning_units"]

            if orga_ids is not None:
                temp = []
                for t in list_of_tasks:
                    if set(t['orga_id']).issubset(set(orga_ids)):
                        temp.append(t)
                
                list_of_tasks = temp

            task_ids = [d["id"] for d in list_of_tasks]
            max_num = len(task_ids)
            
            message = "success"
            data_type = "task"
            
            if num_of_recs < max_num:
                results = random.sample(task_ids, num_of_recs)
            else:
                message = f"Max number of results reached: Requires {num_of_recs} results, {max_num} returned."
                results = task_ids
            
            return {"message": message, "type": data_type, "results": results}, HTTPStatus.OK
        except ValueError as e:
            return e.args, HTTPStatus.BAD_REQUEST
        except TypeError as e:
            return e.args, HTTPStatus.CONFLICT
    

## -------------- get random learning paths --------------------- ##
@ns_random.route("/get-random-paths", endpoint="recsys_get_random_paths")
class GetRandomPaths(Resource):
    @ns_random.expect(parser_random)
    @ns_random.marshal_with(dto_random_response)
    def get(self):
        try:
            # get request data
            request_data = parser_random.parse_args()
            num_of_recs = request_data["num_of_recs"]
            orga_ids = request_data["orga_ids"]

            # fetch paths from SSE-srv
            response = sse_learningpath_api.learning_path_mgmt_controller_get_learning_paths_of_owner()
            
            d = LearningPathListDto(learning_paths=response.learning_paths)
            response_data = d.to_dict()
            list_of_paths = response_data["learning_paths"]
            
            if orga_ids is not None:
                temp = []
                for p in list_of_paths:
                    if set(p['owner']).issubset(set(orga_ids)):
                        temp.append(p)
                
                list_of_paths = temp
            
            pprint(list_of_paths)
            
            path_ids = [d["id"] for d in list_of_paths]
            max_num = len(path_ids)
            
            message = "success"
            data_type = "path"
            
            if num_of_recs < max_num:
                results = random.sample(path_ids, num_of_recs)
            else:
                message = f"Max number of results reached: Requires {num_of_recs} results, {max_num} returned."
                results = path_ids
            
            return {"message": message, "type":data_type, "results": results}, HTTPStatus.OK
        except ValueError as e:
            return e.args, HTTPStatus.BAD_REQUEST
        except TypeError as e:
            return e.args, HTTPStatus.CONFLICT
        