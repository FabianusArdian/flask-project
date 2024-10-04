from db import database, animal_id_counter

# Animal Management Functions
def get_all_animals():
    return list(database['animals'].values())

def get_animal_by_id(animal_id):
    return database['animals'].get(animal_id)

def add_animal(data):
    global animal_id_counter
    animal_id_counter += 1  # Auto-increment ID
    new_animal = {
        "id": str(animal_id_counter),  # Convert to string to maintain consistency
        "species": data.get("species"),
        "age": data.get("age"),
        "gender": data.get("gender"),
        "special_requirements": data.get("special_requirements", "")
    }
    database['animals'][str(animal_id_counter)] = new_animal
    return new_animal

def update_animal(animal_id, data):
    if animal_id in database['animals']:
        animal = database['animals'][animal_id]
        animal.update({
            "species": data.get("species", animal['species']),
            "age": data.get("age", animal['age']),
            "gender": data.get("gender", animal['gender']),
            "special_requirements": data.get("special_requirements", animal['special_requirements'])
        })
        return animal
    return None

def delete_animal(animal_id):
    return database['animals'].pop(animal_id, None)
