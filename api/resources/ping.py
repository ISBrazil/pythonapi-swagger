from flask_restplus import Resource
from api.resources.restplus import api

ns = api.namespace('ping', description='Operations to test the api')

@ns.route('/')
class Ping(Resource):
    def get(self):
        return "pong"