from services.animal_service import get_all_animals, get_animal_by_id, add_animal, update_animal, delete_animal, animal_id_counter

def test_get_all_animals(reset_db):
    animals = get_all_animals()
    assert len(animals) == 3
    assert animals[0]['species'] == "Singa"

def test_get_animal_by_id(reset_db):
    animal = get_animal_by_id("1")
    assert animal is not None
    assert animal['species'] == "Singa"

def test_add_animal(reset_db):
    new_animal = {
        "species": "Gajah",
        "age": 10,
        "gender": "Laki",
        "special_requirements": "Perlu kolam besar"
    }
    animal = add_animal(new_animal)
    assert animal['species'] == "Gajah"

def test_update_animal(reset_db):
    updated_data = {
        "species": "Harimau",
        "age": 5,
        "gender": "Perempuan"
    }
    animal = update_animal("1", updated_data)
    assert animal is not None
    assert animal['species'] == "Harimau"
    assert animal['age'] == 5

def test_delete_animal(reset_db):
    animal = delete_animal("1")
    assert animal is not None
    assert animal['species'] == "Singa"
    assert get_animal_by_id("1") is None
