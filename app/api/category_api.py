from app import app
from typing import Dict, List
from flask import jsonify, wrappers, request
from app.models import Categories
from app.api.users_api import token_required


@app.route('/categories/', methods=['GET'])
def categories() -> Dict[str, List[Dict[str, str]]]:
    return Categories.to_json(dict(Categories.get_categories()))


@app.route('/category/<int:id>', methods=['GET'])
def get_category(id: int) -> Dict[str, List[Dict[str, str]]]:
    category = Categories.query.get_or_404(id)
    return Categories.to_json(dict([[category.category_id,
                                     category.category_name]]))


@app.route('/category/', methods=['POST'])
@token_required
def add_category() -> wrappers.Response:
    category = request.get_json()
    print(category)
    try:
        Categories.add(category)
        return jsonify({"201 Created": "HTTP/1.1"})
    except:
        return jsonify({"403 Forbidden": "HTTP/1.1"})


@app.route('/category/<int:id>', methods=['DELETE'])
@token_required
def delete_category(id: int) -> wrappers.Response:
    Categories.query.get_or_404(id)
    Categories.delete_note(id)
    return jsonify({"200 OK": "HTTP/1.1"})


@app.route('/category/<int:id>', methods=['PUT'])
@token_required
def edit_category(id: int) -> wrappers.Response:
    Categories.query.get_or_404(id)
    try:
        Categories.edit(request.get_json(), id)
        return jsonify({"200 OK": "HTTP/1.1"})
    except:
        return jsonify({"403 Forbidden": "HTTP/1.1"})

