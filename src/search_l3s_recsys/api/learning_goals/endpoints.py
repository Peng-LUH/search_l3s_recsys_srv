from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask_cors import cross_origin


sys.path.append('..')

from search_l3s_recsys.api.learning_goals.dto import (
      dto_learning_goals_recommend_response_item,
      dto_learning_goals_recommend_response

)



ns_learning_goals_rec = Namespace("LearningGoalsRec", validate=True)

ns_learning_goals_rec.models[dto_learning_goals_recommend_response_item.name] = dto_learning_goals_recommend_response_item
ns_learning_goals_rec.models[dto_learning_goals_recommend_response.name] = dto_learning_goals_recommend_response


@ns_learning_goals_rec.route("/<string:user_id>/learning-goals/", endpoint="learning-goals-recommendation")
class RecLearningGoals(Resource):   
    @ns_learning_goals_rec.marshal_with(dto_learning_goals_recommend_response)  
    def get(self, user_id):   
            "get recommendations based on user's learning goals"     
            
            from search_l3s_recsys.api.learning_goals.logic import LearningGoalsRec
            learning_goals = LearningGoalsRec()
    
            results = {
                 "entity_id": "string",
                 "entity_type": "string",
                 "owner": "string",
                 "similarity": 1.0,
                 "user_id": user_id
                    }
            

            try:
                  results = learning_goals.recommend(user_id)
                  assert len(results)>0, "No recommendations available"
                  return {"message": "success", "results": results}, HTTPStatus.OK

            except ValueError as e:
                return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
            except FileExistsError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
            except AssertionError as e:
                    return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR     
    




