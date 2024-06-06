from flask_restx import Model, fields


dto_jobs_search_request = Model("DtoJobsSearchRequest", {
    "loc": fields.String(description="location for searching jobs", default=None, required=True),
    "job_name": fields.String(description="job name", default=None),
    "radius": fields.String(description="radius in which we are searching jobs", default=50)
})

dto_skills_request = Model("DtoSkillsRequest", {
    "loc": fields.String(),
    "job_name": fields.String(),
    "radius": fields.Integer()
})

dto_trending_skills_request = Model("DtoTrendingSkillsRequest", {
    "loc": fields.String(),
    "job_name": fields.String(),
    "radius": fields.Integer()
})




dto_trending_skills_response_item = Model("DtoTrendingSkillsResponseItem", {
    "topk": fields.String(description='number of top Trending Skills', example=5),
    "trending_skills": fields.List(fields.String, description='List of Trending Skills', example=["Kundenberatung, -betreuung",
    "Abrechnung",
    "Kosten- und Leistungsrechnung",
    "Akquisition",
    "Korrespondenz"])
})

dto_trending_skills_response = Model('DtoTrendingSkillsResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_trending_skills_response_item, description='Results')
                                        })




dto_trends_recommend_response_item= Model('DtoTrendsRecommendResponseItem', {
    'entity_id': fields.String(required=True, description='The entity ID', example="1"),
    'entity_type': fields.String(required=True, description='The entity type', example="skill"),
    'owner': fields.String(required=False, description='The owner list', example=["1"]),
    'similarity': fields.Float(required=False, description='The similarity value', example=0.920),
    'user_id': fields.String(required=False, description='The user ID', default="1", example="1"),
})



dto_trends_recommend_response = Model("DtoTrendsRecommendResponse", {
    'message': fields.String(required=True, example="success", description='Success message'),
    'results': fields.List(fields.Nested(dto_trends_recommend_response_item)),                               
})

