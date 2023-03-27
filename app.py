import os

from flask import Flask, request, jsonify
from marshmallow import ValidationError


from constructor import constructor_query
from models import BatchRequestParams

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():
    try:
        params = BatchRequestParams().load(data=request.json)
    except ValidationError as error:
        return jsonify(error.messages), 400

    result = None
    for query in params['queries']:
        result = constructor_query(
            cmd=query['cmd'],
            value=query['value'],
            data=result,
        )

    return jsonify(result)





app.run()