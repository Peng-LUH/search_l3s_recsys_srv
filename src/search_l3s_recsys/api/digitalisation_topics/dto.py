from flask_restx import Model, fields


dto_digitalisation_topics_response_item = Model("DtoDigiTopicsResponseItem", {
    "topk": fields.String(description='number of top Trending Skills', example=5),
    "trending_skills": fields.List(fields.String, description='List of Trending Skills', example=["Kundenberatung, -betreuung",
    "Abrechnung",
    "Kosten- und Leistungsrechnung",
    "Akquisition",
    "Korrespondenz"])
})

dto_digitalisation_topics_response = Model('DtoDigiTopicsResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_digitalisation_topics_response_item, description='Results')
                                        })




dto_digitalisation_topics_recommend_response_item= Model('DtoDigiTopicsRecommendResponseItem', {
    'entity_id': fields.String(required=True, description='The entity ID', example="1"),
    'entity_type': fields.String(required=True, description='The entity type', example="skill"),
    'owner': fields.String(required=False, description='The owner list', example=["1"]),
    'similarity': fields.Float(required=False, description='The similarity value', example=0.920),
    'user_id': fields.String(required=False, description='The user ID', default="1", example="1"),
})



dto_digitalisation_topics_recommend_response = Model("DtoDigiTopicsRecommendResponse", {
    'message': fields.String(required=True, example="success", description='Success message'),
    'results': fields.List(fields.Nested(dto_digitalisation_topics_recommend_response_item)),                               
})

