from flask import Blueprint, jsonify

from src.errors.error_handler import handle_errors
from src.main.composer.pet_deleter_composer import pet_deleter_composer
from src.main.composer.pet_lister_composer import pet_lister_composer
from src.views.http_types.http_request import HttpRequest

pet_route_pb = Blueprint("pets_routes", __name__)


@pet_route_pb.route("/pets", methods=["GET"])
def list_pets():
    try:
        http_request = HttpRequest()
        view = pet_lister_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exc:
        http_response = handle_errors(exc)
        return jsonify(http_response.body), http_response.status_code


@pet_route_pb.route("/pets/<name>", methods=["DELETE"])
def delete_pets(name: str):
    try:
        http_request = HttpRequest(param={"name": name})
        view = pet_deleter_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exc:
        http_response = handle_errors(exc)
        return jsonify(http_response.body), http_response.status_code
