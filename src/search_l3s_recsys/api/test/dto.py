from flask_restx import Model, fields

test_model = Model("test", {
    "message": fields.String(required=True)
})