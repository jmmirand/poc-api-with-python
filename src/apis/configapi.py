from flask import jsonify, request
from flask_restplus import Namespace, Resource, fields

api = Namespace('API Config', description='This config permit view current config')

@api.route("/")
class Teams(Resource):
    @api.doc(description='Read Global Config')
    def get(self):
        result = ["Config Readed"]
        return jsonify(result)