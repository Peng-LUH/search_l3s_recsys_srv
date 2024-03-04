from flask_restx import Model, fields

# dto_random_request = Model("DtoRandomRequest", {
#     "num_of_rec": fields.Integer(required=True, default=10)
# })

dto_random_response = Model("DtoRandomResponse", {
    "message": fields.String(required=True),
    "type": fields.String(required=True),
    "results": fields.List(fields.String, required=True)
})