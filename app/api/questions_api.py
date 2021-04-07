from app import app
from typing import Dict, List
from flask import jsonify, wrappers, request
from app.models import Questions
from app.api.users_api import token_required


@app.route('/questions/', methods=['GET'])
def questions() -> Dict[str, List[Dict[str, str]]]:
    return Questions.to_json(dict(Questions.get_questions()))


@app.route('/question', methods=['POST'])
@token_required
def add_question() -> wrappers.Response:
    question = request.get_json()
    print(question)
    try:
        Questions.add(question)
        return jsonify({"201 Created": "HTTP/1.1"})
    except:
        return jsonify({"403 Forbidden": "HTTP/1.1"})


@app.route('/question/<int:id>', methods=['DELETE'])
@token_required
def delete_question(id: int) -> wrappers.Response:
    Questions.query.get_or_404(id)
    try:
        Questions.delete_note(id)
        return jsonify({"200 OK": "HTTP/1.1"})
    except:
        return jsonify({"403 Forbidden": "HTTP/1.1"})


@app.route('/question/<int:id>', methods=['PUT'])
@token_required
def edit_question(id: int) -> wrappers.Response:
    Questions.query.get_or_404(id)
    try:
        Questions.edit(request.get_json(), id)
        return jsonify({"200 OK": "HTTP/1.1"})
    except:
        return jsonify({"403 Forbidden": "HTTP/1.1"})
