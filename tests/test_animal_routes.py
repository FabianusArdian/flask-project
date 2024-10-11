def test_get_animals(client):
    response = client.get("/animals/")
    assert response.status_code == 200
    assert b"Singa" in response.data

def test_get_animal(client):
    response = client.get("/animals/1")
    assert response.status_code == 200
    assert b"Singa" in response.data

def test_create_animal(client):
    new_animal = {
        "species": "Gajah",
        "age": 10,
        "gender": "Laki",
        "special_requirements": "Perlu kolam besar"
    }
    response = client.post("/animals/", json=new_animal)
    assert response.status_code == 201
    assert b"Gajah" in response.data

def test_update_animal(client):
    updated_animal = {
        "species": "Singa",
        "age": 3,
        "gender": "Perempuan",
        "special_requirements": "Perlu kandang besar"
    }
    response = client.put("/animals/1", json=updated_animal)
    assert response.status_code == 200
    assert b"Perempuan" in response.data

def test_delete_animal(client):
    response = client.delete("/animals/1")
    assert response.status_code == 200
    assert b"Animal deleted successfully" in response.data
