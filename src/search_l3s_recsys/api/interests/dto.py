from flask_restx import Model, fields


                        
dto_interest_recommend_response_item= Model('DtoInterestRecommendResponseItem', {
    'entity_id': fields.String(required=True, description='The entity ID', example="1"),
    'entity_type': fields.String(required=True, description='The entity type', example="skill"),
    'owner': fields.String(required=False, description='The owner list', example=["1"]),
    'similarity': fields.Float(required=False, description='The similarity value', example=0.920),
    'user_id': fields.String(required=False, description='The user ID', default="1", example="1"),
})



dto_interest_recommend_response = Model("DtoInterestRecommendResponse", {
    'message': fields.String(required=True, example="success", description='Success message'),
    'results': fields.List(fields.Nested(dto_interest_recommend_response_item)),                               
})

