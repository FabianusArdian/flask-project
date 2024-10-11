def test_get_employees(client, reset_db):
    response = client.get("/employees/")
    assert response.status_code == 200
    assert b"Pevita Piss" in response.data

def test_get_employee(client, reset_db):
    response = client.get("/employees/1")
    assert response.status_code == 200
    assert b"Pevita Piss" in response.data

def test_create_employee(client, reset_db):
    new_employee = {
        "name": "Rina Andriani",
        "email": "rina@safari.com",
        "phone": "+6211111",
        "role": "Dokter Hewan",
        "schedule": "Mon-Fri, 8AM-4PM"
    }
    response = client.post("/employees/", json=new_employee)
    assert response.status_code == 201
    assert b"Rina Andriani" in response.data

def test_update_employee(client, reset_db):
    updated_employee = {
        "name": "Bambang Kirun",
        "email": "bambangk@safari.com",
        "phone": "+6214321",
        "role": "Manager",
        "schedule": "Mon-Fri, 9AM-5PM"
    }
    response = client.put("/employees/2", json=updated_employee)
    assert response.status_code == 200
    assert b"Manager" in response.data

def test_delete_employee(client, reset_db):
    response = client.delete("/employees/2")
    assert response.status_code == 200
    assert b"Employee deleted successfully" in response.data
