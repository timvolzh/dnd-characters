import json

import flask
from cffi.backend_ctypes import unicode
from flask import Flask, request
from flask.views import MethodView

from modules.base import CharDB

app = Flask('apps')
app.config['JSON_AS_ASCII'] = False


@app.route('/home')
def home():
    return flask.jsonify({'status': 'works'})


'''___Views___'''


class CharView(MethodView):

    def __init__(self):
        self.db = CharDB()

    def post(self):
        data = request.json
        try:
            response = self.db.create_char(data)
            return flask.jsonify({"Result": f"{response}"})
        except Exception as ex:
            return flask.jsonify({"Exception": f"{ex}"})

    def get(self, char_name: str):
        try:
            char = self.db.find_by_name(char_name)
            # char = {k: unicode(v).encode("utf-8") for k, v in char.items()}
        except Exception as ex:
            raise HttpError(404, str(ex))
        return flask.jsonify(char)


'''___Exceptions___'''


class HttpError(Exception):

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message


@app.errorhandler(HttpError)
def handle_http_error(error):
    response = flask.jsonify({'message': error.message})
    response.status_code = error.status_code
    return response


'''___Bindings___'''

app.add_url_rule(
    '/char/<char_name>', view_func=CharView.as_view('char_api_get'), methods=['GET'])
app.add_url_rule(
    '/char/', view_func=CharView.as_view('char_api_post'), methods=['POST'])

app.run()
