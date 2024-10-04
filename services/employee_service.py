from db import database, employee_id_counter

def get_all_employees():
    return list(database['employees'].values())

def get_employee_by_id(employee_id):
    return database['employees'].get(employee_id)

def add_employee(data):
    global employee_id_counter
    employee_id_counter += 1
    new_employee = {
        "id": str(employee_id_counter),
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "role": data.get("role"),
        "schedule": data.get("schedule", "")
    }
    database['employees'][str(employee_id_counter)] = new_employee
    return new_employee

def update_employee(employee_id, data):
    if employee_id in database['employees']:
        employee = database['employees'][employee_id]
        employee.update({
            "name": data.get("name", employee['name']),
            "email": data.get("email", employee['email']),
            "phone": data.get("phone", employee['phone']),
            "role": data.get("role", employee['role']),
            "schedule": data.get("schedule", employee['schedule'])
        })
        return employee
    return None

def delete_employee(employee_id):
    return database['employees'].pop(employee_id, None)
