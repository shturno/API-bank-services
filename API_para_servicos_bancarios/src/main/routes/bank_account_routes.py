from flask import Blueprint, request, jsonify

bank_routes_bp = Blueprint("bank_routes", __name__)

@bank_routes_bp.route("/", methods=[""])