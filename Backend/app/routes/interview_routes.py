# app/routes/interview_routes.py
from flask import Blueprint, request, jsonify
from app.services.ai_service import ask_ai

interview_bp = Blueprint("interview", __name__, url_prefix="/api/interview")

@interview_bp.route("/question", methods=["POST"])
def get_question():
    data = request.get_json()
    if not data or "role" not in data:
        return jsonify({"error": "Missing 'role' in request body"}), 400

    role = data["role"]
    questions = ask_ai(role)  # Calls our mock service

    return jsonify({"questions": questions})
