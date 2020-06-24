from api.resources.restplus import api
from flask_restplus import fields

type_product_serializer = api.model('Product', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a product post'),
    'description': fields.String(required=True, description='Name product'),
})