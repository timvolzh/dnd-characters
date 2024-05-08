
import flask
from flask import Flask, request
from flask.views import MethodView

from modules.base import MongoDB, CharDB

app = Flask('app')

@app.route('/home')
def home():
    return flask.jsonify({'status': 'works'})

'''
@app.errorhandler(HttpError)
def handle_http_error(error):
    response = flask.jsonify({'message': error.message})
    response.status_code = error.status_code
    return response
'''


app.run()

