from flask_restx import Model, fields

random_request_model = Model("RandomRequest", {
    "num_of_rec": fields.Integer(required=True, default=10)
})

random_response_model = Model("RandomResponse", {
    "id": fields.String(required=True, attribute='@id')
})