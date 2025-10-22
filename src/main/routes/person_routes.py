from flask import Blueprint, jsonify, request

from src.errors.error_handler import handle_errors
from src.main.composer.person_creator_composer import person_creator_composer
from src.main.composer.person_finder_composer import person_finder_composer
from src.views.http_types import HttpRequest

person_route_pb = Blueprint("person_routes", __name__)


@person_route_pb.route("/person", methods=["POST"])
def create_person():
    try:
        http_request = HttpRequest(request.json)
        view = person_creator_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exc:
        http_response = handle_errors(exc)
        return jsonify(http_response.body), http_response.status_code


@person_route_pb.route("/people/<int:person_id>", methods=["GET"])
def find_person(person_id: int):
    try:
        http_request = HttpRequest(param={"person_id": person_id})
        view = person_finder_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exc:
        http_response = handle_errors(exc)
        print(http_response.body)
        return jsonify(http_response.body), http_response.status_code
