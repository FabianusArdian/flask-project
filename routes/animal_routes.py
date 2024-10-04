from flask import Blueprint, jsonify, request, abort
from services.animal_service import get_all_animals, get_animal_by_id, add_animal, update_animal, delete_animal

animal_bp = Blueprint('animal_bp', __name__)

@animal_bp.route('/', methods=['GET'])
def get_animals():
    """
    Retrieve a list of all animals in the zoo.
    ---
    responses:
      200:
        description: A list of animals
    """
    return jsonify(get_all_animals()), 200

@animal_bp.route('/<id>', methods=['GET'])
def get_animal(id):
    """
    Retrieve a specific animal by id (Auto Increment).
    ---
    parameters:
      - name: id
        in: path
        type: integer    # Specify the type as integer for Auto Increment
        required: true
        description: The animal ID (Auto Increment)
    responses:
      200:
        description: Animal details
      404:
        description: Animal not found
    """
    animal = get_animal_by_id(id)
    if animal:
        return jsonify(animal), 200
    return abort(404, description="Animal not found")

@animal_bp.route('/', methods=['POST'])
def create_animal():
    """
    Add a new animal to the zoo.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - species
            - age
            - gender
          properties:
            species:
              type: string
            age:
              type: integer
            gender:
              type: string
            special_requirements:
              type: string
    responses:
      201:
        description: Animal created
    """
    data = request.json
    new_animal = add_animal(data)
    return jsonify(new_animal), 201

@animal_bp.route('/<id>', methods=['PUT'])
def update_animal_route(id):
    """
    Update an existing animal by id (Auto Increment).
    ---
    parameters:
      - name: id
        in: path
        type: integer    # Specify the type as integer for Auto Increment
        required: true
        description: The animal ID (Auto Increment)
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            species:
              type: string
            age:
              type: integer
            gender:
              type: string
            special_requirements:
              type: string
    responses:
      200:
        description: Animal updated
      404:
        description: Animal not found
    """
    data = request.json
    updated_animal = update_animal(id, data)
    if updated_animal:
        return jsonify(updated_animal), 200
    return abort(404, description="Animal not found")

@animal_bp.route('/<id>', methods=['DELETE'])
def delete_animal_route(id):
    """
    Delete an existing animal by id (Auto Increment).
    ---
    parameters:
      - name: id
        in: path
        type: integer    # Specify the type as integer for Auto Increment
        required: true
        description: The animal ID (Auto Increment)
    responses:
      200:
        description: Animal deleted successfully
      404:
        description: Animal not found
    """
    deleted_animal = delete_animal(id)
    if deleted_animal:
        return jsonify({"message": "Animal deleted successfully"}), 200
    return abort(404, description="Animal not found")
