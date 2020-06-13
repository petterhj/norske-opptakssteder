from flask import jsonify
from flask_restful import Api

from endpoints.productions import Productions
from endpoints.people import People


class NorlocApi(Api):
    def handle_error(self, e):
        message = e.description
        if e.code == 404:
            message = "Resource not found"
        return jsonify({"status_code": e.code, "message": message}), e.code


norloc_api = NorlocApi(catch_all_404s=True)
norloc_api.add_resource(Productions, *(
    '/productions',
    '/productions/<string:slug>'
))
norloc_api.add_resource(People, *(
    '/people', 
    '/people/<string:slug>'
))
