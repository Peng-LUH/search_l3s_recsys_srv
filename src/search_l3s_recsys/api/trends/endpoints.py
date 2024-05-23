from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask_cors import cross_origin


sys.path.append('..')

from search_l3s_recsys.api.trends.dto import (
    dto_trending_skills_response_item,
    dto_trending_skills_response,
    dto_trends_recommend_response,
    dto_trends_recommend_response_item,
)



ns_trends = Namespace("Trends", validate=True)

ns_trends.models[dto_trending_skills_response_item.name] = dto_trending_skills_response_item
ns_trends.models[dto_trending_skills_response.name] = dto_trending_skills_response
ns_trends.models[dto_trends_recommend_response_item.name] = dto_trends_recommend_response_item
ns_trends.models[dto_trends_recommend_response.name] = dto_trends_recommend_response


parser_trends = ns_trends.parser()
parser_trends.add_argument('loc', type=str, required=True, help='location for searching job', default="berlin")
parser_trends.add_argument('job_name', type=str, required=True,help="job name", default="machine learning")
parser_trends.add_argument('topk', type=int, required=True, help='top k trending skills', default=5)

@ns_trends.route("/trending-skills/", endpoint="trending-skills")
class GetTrendingSkills(Resource):   
    @ns_trends.marshal_with(dto_trending_skills_response)  
    @ns_trends.expect(parser_trends)
    def get(self):   
            "get trending skills"     

            args = parser_trends.parse_args()
            loc, job_name, topk = args['loc'], args['job_name'], args['topk']
            
            assert topk>0, "Invalid topk. Please use topk greater than 0."    

            from search_l3s_recsys.api.trends.logic_bfn import TrendSkillsBfn
            trend = TrendSkillsBfn()
    
            results = {
                 "topk": topk,
                 "trending_skills": []
                    }

            try:
                  output = trend.trending_skills(job_name, topk)
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
    


parser_recommend_trends = ns_trends.parser()
parser_recommend_trends.add_argument('loc', type=str, required=True, help='location for searching job', default="berlin")
parser_recommend_trends.add_argument('job_name', type=str, required=True,help="job name", default="machine learning")
parser_recommend_trends.add_argument('topk', type=int, required=True, help='top k trending skills', default=5)
parser_recommend_trends.add_argument('user_id', type=str, required=True, help='id of the user', default="1")
parser_recommend_trends.add_argument('owner', type=str, required=True, help='owner', default="1")

@ns_trends.route("/trending-recommend/", endpoint="recommend-trendings")
class GetRecommendTrends(Resource):   
    @ns_trends.marshal_with(dto_trends_recommend_response)  
    @ns_trends.expect(parser_recommend_trends)
    def get(self):   
            "recommend trending skills, tasks, and learning paths"     

            args = parser_recommend_trends.parse_args()
            user_id, job_name,  topk = args['user_id'], args['job_name'],  args['topk']
            
            from search_l3s_recsys.api.trends.logic_bfn import TrendSkillsBfn
            trend = TrendSkillsBfn()

            results = {
                 "entity_id": "string",
                 "entity_type": "string",
                 "owner": "string",
                 "similarity": 1.0,
                 "user_id": user_id
                    }
            
            try:
                  assert topk>0, "Invalid topk. Please use topk greater than 0."     
                  results = trend.recommend(job_name,topk, user_id)
                  return {"message": "success", "results": results}, HTTPStatus.OK

            except ValueError as e:
                return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
            except FileExistsError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
            except AssertionError as e:
                    return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR     
    


@ns_trends.route("/trending-tasks/", endpoint="trending_tasks")
class TrendingTasks(Resource):
      def get(self):
            '''get trending tasks/learning units'''
            return {"message": "not implemented"}, HTTPStatus.OK
      

@ns_trends.route("/trending-paths/", endpoint="trending_paths")
class TrendingPaths(Resource):
      def get(self):
            '''get trending learning paths'''
            return {"message": "not implemented"}, HTTPStatus.OK
