from services.employee_service import get_all_employees, get_employee_by_id, add_employee, update_employee, delete_employee

def test_get_all_employees(reset_db):
    employees = get_all_employees()
    assert len(employees) == 3
    assert employees[0]['name'] == "Pevita Piss"

def test_get_employee_by_id(reset_db):
    employee = get_employee_by_id("1")
    assert employee is not None
    assert employee['name'] == "Pevita Piss"

def test_add_employee(reset_db):
    new_employee = {
        "name": "Rina Andriani",
        "email": "rina@safari.com",
        "phone": "+6211111",
        "role": "Dokter Hewan",
        "schedule": "Mon-Fri, 8AM-4PM"
    }
    employee = add_employee(new_employee)
    assert employee['name'] == "Rina Andriani"

def test_update_employee(reset_db):
    updated_data = {
        "name": "Bambang Kirun",
        "email": "bambangk@zoo.com",
        "phone": "+6214321",
        "role": "Manager"
    }
    employee = update_employee("2", updated_data)
    assert employee is not None
    assert employee['name'] == "Bambang Kirun"
    assert employee['role'] == "Manager"

def test_delete_employee(reset_db):
    employee = delete_employee("1")
    assert employee is not None
    assert employee['name'] == "Pevita Piss"
    assert get_employee_by_id("1") is None
