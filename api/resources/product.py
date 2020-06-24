# istanbul ignore file

from flask_restplus import reqparse, Resource
from api.controllers.product import Product_Controller
from api.resources.restplus import api
from api.model.modelAPI import type_product_serializer

parser = reqparse.RequestParser()
parser.add_argument('id', help='ID of product <br> type: int', required=True)
parser.add_argument('description', help='description of a product <br> type: string', required=True)

ns = api.namespace('api/product', description='Operations related to product')

@ns.route('/')
class Product(Resource):
    @api.response(200, 'success', type_product_serializer)
    def get(self):
        type_product_controller = Product_Controller()
        return type_product_controller.find_all()
        
    @api.expect(parser)
    @api.response(200, 'success', type_product_serializer)
    def post(self):
        data = parser.parse_args()
        type_product_controller = Product_Controller()
        insert = type_product_controller.insert_type_problem(data)
        return insert

@ns.route('/<int:id>')
class Product_Id(Resource):
    @api.doc(params={'id': 'And ID of product'})
    def get(self, id):
        type_problem_controller = Product_Controller()
        return type_problem_controller.find_one(id)