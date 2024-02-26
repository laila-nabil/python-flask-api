from flask import Flask, jsonify, request
import controller
from db import create_tables

app = Flask(__name__)


@app.route('/test_cases', methods=["GET"])
def get_test_cases():
    test_cases = controller.get_test_Cases()
    return jsonify(test_cases)


@app.route("/test_case", methods=["POST"])
def insert_test_case():
    test_case_details = request.get_json()
    title = test_case_details["title"]
    steps = test_case_details["steps"]
    expected_result = test_case_details["expected_result"]
    actual_result = test_case_details["actual_result"]
    test_assets = test_case_details["test_assets"]
    status = test_case_details["status"]
    response = controller.insert_test_case(title, steps , expected_result , actual_result , test_assets, status)
    return jsonify(response)


@app.route("/test_case", methods=["PUT"])
def update_test_case():
    test_case_details = request.get_json()
    id = test_case_details["id"]
    title = test_case_details["title"]
    steps = test_case_details["steps"]
    expected_result = test_case_details["expected_result"]
    actual_result = test_case_details["actual_result"]
    test_assets = test_case_details["test_assets"]
    status = test_case_details["status"]
    response = controller.update_test_case(id, title, steps , expected_result , actual_result, test_assets, status)
    return jsonify(response)


@app.route("/test_case/<id>", methods=["DELETE"])
def delete_test_case(id):
    response = controller.delete_test_case(id)
    return jsonify(response)


@app.route("/test_case/<id>", methods=["GET"])
def get_test_case_by_id(id):
    test_case = controller.get_by_id(id)
    return jsonify(test_case)


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(debug=False)
