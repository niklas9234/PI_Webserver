from flask import Blueprint, request, jsonify, render_template

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    return jsonify({"message": "Login erfolgreich", "data": data})


