from flask import Flask, request, jsonify
from marshmallow import ValidationError

from constants import DATA_DIR
from models import RequestSchema
from utils import build_query

app = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query():
    data = request.args
    try:
        validated_data = RequestSchema().load(data)
    except ValidationError as ex:
        return jsonify(ex.messages), 400

    first_commands = build_query(
        cmd=validated_data["cmd1"],
        value=validated_data["value1"],
        file=DATA_DIR + validated_data["file_name"],
        data=None
    )

    result = build_query(
        cmd=validated_data["cmd2"],
        value=validated_data["value2"],
        file=DATA_DIR + validated_data["file_name"],
        data=first_commands
    )

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
