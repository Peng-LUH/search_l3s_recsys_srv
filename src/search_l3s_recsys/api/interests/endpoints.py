from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask_cors import cross_origin


sys.path.append('..')

from search_l3s_recsys.api.interests.dto import (
    dto_interest_recommend_response_item,
    dto_interest_recommend_response
)


ns_interests_rec = Namespace("InterestsRec", validate=True)

ns_interests_rec.models[dto_interest_recommend_response_item.name] = dto_interest_recommend_response_item
ns_interests_rec.models[dto_interest_recommend_response.name] = dto_interest_recommend_response

@ns_interests_rec.route("/<string:user_id>/interests/", endpoint="recommend-interests")
class RecInterests(Resource):   
    @ns_interests_rec.marshal_with(dto_interest_recommend_response)  
    def get(self, user_id):   
            "get recommendation based on user's interests"     
            

            from search_l3s_recsys.api.interests.logic import InterestRec
            int_rec = InterestRec()
    
            results = {
                 "entity_id": "string",
                 "entity_type": "string",
                 "owner": "string",
                 "similarity": 1.0,
                 "user_id": user_id
                    }
            
            try:
                  results = int_rec.recommend(user_id)
                  assert len(results)>0, "Nothing to Recommend."
                  return {"message": "success", "results": results}, HTTPStatus.OK

            except ValueError as e:
                return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
            except FileExistsError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
            except AssertionError as e:
                    return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR     
    


