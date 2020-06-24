import json
from api.model.modelAPI import type_product_serializer
# istanbul ignore file
class Product_Controller():
    
    def find_all(self):
        with open("api/model/Model.json","r") as json_file:
            data = json.load(json_file)
        return {'status': 'success', 'data': data}, 200

    def find_one(self, id):
        with open("api/model/Model.json","r") as json_file:
            data = json.load(json_file)

        for x in data['product']:
            if x["id"] == str(id):
                data = x
        return {'status': 'success', 'data': data}, 200

    def insert_type_problem(self, info):
        with open("api/model/Model.json","r") as json_file:
            data = json.load(json_file)
        data["product"].append(info)

        with open("api/model/Model.json","w") as json_file:
            json.dump(data, json_file)
        return {'status': 'success', 'data': "OK"}, 200