from flask import Blueprint, jsonify, request, abort
from services.employee_service import get_all_employees, get_employee_by_id, add_employee, update_employee, delete_employee

employee_bp = Blueprint('employee_bp', __name__)

@employee_bp.route('/', methods=['GET'])
def get_employees():
    """
    Retrieve a list of all employees in the zoo.
    ---
    responses:
      200:
        description: A list of employees
    """
    return jsonify(get_all_employees()), 200

@employee_bp.route('/<id>', methods=['GET'])
def get_employee(id):
    """
    Retrieve a specific employee by id.
    ---
    parameters:
      - name: id
        in: path
        type: integer    # Specify the type as integer for Auto Increment
        required: true
        description: The employee ID (Auto Increment)
    responses:
      200:
        description: Employee details
      404:
        description: Employee not found
    """
    employee = get_employee_by_id(id)
    if employee:
        return jsonify(employee), 200
    return abort(404, description="Employee not found")

@employee_bp.route('/', methods=['POST'])
def create_employee():
    """
    Add a new employee to the zoo.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - email
            - phone
            - role
          properties:
            name:
              type: string
            email:
              type: string
            phone:
              type: string
            role:
              type: string
            schedule:
              type: string
    responses:
      201:
        description: Employee created
    """
    data = request.json
    new_employee = add_employee(data)
    return jsonify(new_employee), 201

@employee_bp.route('/<id>', methods=['PUT'])
def update_employee_route(id):
    """
    Update an existing employee by id.
    ---
    parameters:
      - name: id
        in: path
        type: integer    # Specify the type as integer for Auto Increment
        required: true
        description: The employee ID (Auto Increment)
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
            phone:
              type: string
            role:
              type: string
            schedule:
              type: string
    responses:
      200:
        description: Employee updated
      404:
        description: Employee not found
    """
    data = request.json
    updated_employee = update_employee(id, data)
    if updated_employee:
        return jsonify(updated_employee), 200
    return abort(404, description="Employee not found")

@employee_bp.route('/<id>', methods=['DELETE'])
def delete_employee_route(id):
    """
    Delete an existing employee by id.
    ---
    parameters:
      - name: id
        in: path
        type: integer    # Specify the type as integer for Auto Increment
        required: true
        description: The employee ID (Auto Increment)
    responses:
      200:
        description: Employee deleted successfully
      404:
        description: Employee not found
    """
    deleted_employee = delete_employee(id)
    if deleted_employee:
        return jsonify({"message": "Employee deleted successfully"}), 200
    return abort(404, description="Employee not found")
