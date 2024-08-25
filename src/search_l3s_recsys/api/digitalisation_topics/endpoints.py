from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask_cors import cross_origin


sys.path.append('..')

from search_l3s_recsys.api.digitalisation_topics.dto import (
    dto_digitalisation_topics_response_item,
    dto_digitalisation_topics_response,
    dto_digitalisation_topics_recommend_response_item,
    dto_digitalisation_topics_recommend_response
)



ns_digi_topics = Namespace("DigitalTopicsRec", validate=True)

ns_digi_topics.models[dto_digitalisation_topics_response_item.name] = dto_digitalisation_topics_response_item
ns_digi_topics.models[dto_digitalisation_topics_response.name] = dto_digitalisation_topics_response
ns_digi_topics.models[dto_digitalisation_topics_recommend_response_item.name] = dto_digitalisation_topics_recommend_response_item
ns_digi_topics.models[dto_digitalisation_topics_recommend_response.name] = dto_digitalisation_topics_recommend_response


parser_digi_topics = ns_digi_topics.parser()
parser_digi_topics.add_argument('loc', type=str, required=True, help='location for searching job', default="berlin")
parser_digi_topics.add_argument('job_name', type=str, required=True,help="job name", default="machine learning")
parser_digi_topics.add_argument('topk', type=int, required=True, help='top k trending skills', default=5)

@ns_digi_topics.route("/trending-digitalisation-topics/", endpoint="digitalisation-topics")
class GetTrendingSkills(Resource):   
    @ns_digi_topics.marshal_with(dto_digitalisation_topics_response)  
    @ns_digi_topics.expect(parser_digi_topics)
    def get(self):   
            "get trending digital topics"     

            args = parser_digi_topics.parse_args()
            loc, job_name, topk = args['loc'], args['job_name'], args['topk']
            
            assert topk>0, "Invalid topk. Please use topk greater than 0."    

            from search_l3s_recsys.api.digitalisation_topics.logic import DigiTopicsBfn
            digi = DigiTopicsBfn()
    
            results = {
                 "topk": topk,
                 "trending_skills": []
                    }
            try:
                  output = digi.digitalisation_topics_by_query(job_name, topk)
                  assert len(output)>0, "No trending skills found"
                  trending_skills = [skill for skill,_ in output]
                  results["trending_skills"] = trending_skills
                  return {"message": "success", "results": results}, HTTPStatus.OK

            except ValueError as e:
                return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
            except FileExistsError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
            except AssertionError as e:
                    return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR     
    


parser_recommend_digi_topics = ns_digi_topics.parser()
parser_recommend_digi_topics.add_argument('loc', type=str, required=True, help='location for searching job', default="berlin")
parser_recommend_digi_topics.add_argument('job_name', type=str, required=True,help="job name", default="machine learning")
parser_recommend_digi_topics.add_argument('topk', type=int, required=True, help='top k trending skills', default=5)
parser_recommend_digi_topics.add_argument('user_id', type=str, required=True, help='id of the user', default="1")
parser_recommend_digi_topics.add_argument('owner', type=str, required=True, help='owner', default="1")

@ns_digi_topics.route("/<string:user_id>/digitalisation-topics/", endpoint="recommend-digitalisation-topics")
class GetRecommendTrends(Resource):   
    @ns_digi_topics.marshal_with(dto_digitalisation_topics_recommend_response)  
    @ns_digi_topics.expect(parser_recommend_digi_topics)
    def get(self):   
            "recommend based on trending digitalisation topics"     

            args = parser_recommend_digi_topics.parse_args()
            user_id, job_name,  topk = args['user_id'], args['job_name'],  args['topk']
            
            from search_l3s_recsys.api.digitalisation_topics.logic import DigiTopicsBfn
            digi = DigiTopicsBfn()

            results = {
                 "entity_id": "string",
                 "entity_type": "string",
                 "owner": "string",
                 "similarity": 1.0,
                 "user_id": user_id
                    }
            
            try:
                  assert topk>0, "Invalid topk. Please use topk greater than 0."     
                  results = digi.recommend_digi_topics(job_name,topk, user_id)
                  return {"message": "success", "results": results}, HTTPStatus.OK

            except ValueError as e:
                return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
            except FileExistsError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
            except AssertionError as e:
                    return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR     
    


# @ns_digi_topics.route("/<string:user_id>/digitalisation-topics-tasks/", endpoint="digitalisation-topics-tasks")
# class TrendingTasks(Resource):
#       def get(self):
#             '''get digitalisation topics -> learning units'''
#             return {"message": "not implemented"}, HTTPStatus.OK
      

# @ns_digi_topics.route("/<string:user_id>/digitalisation-topics-paths/", endpoint="digitalisation-topics-paths")
# class TrendingPaths(Resource):
#       def get(self):
#             '''get digitalisation topics -> learning paths'''
#             return {"message": "not implemented"}, HTTPStatus.OK

