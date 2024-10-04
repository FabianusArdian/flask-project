database = {
    "animals": {
        "1": {
            "id": "1",
            "species": "Singa",
            "age": 2,
            "gender": "Laki",
            "special_requirements": "Perlu Kandang dengan keamanan yang baik"
        },
        "2": {
            "id": "2",
            "species": "Simpanse",
            "age": 5,
            "gender": "Perempuan",
            "special_requirements": "Perlu pepohonan dan tempat bermain"
        },
        "3": {
            "id": "3",
            "species": "Panda",
            "age": 3,
            "gender": "Laki",
            "special_requirements": "Perlu taman bambu dan tempat bermain"
        }
    },
    "employees": {
        "1": {
            "id": "1",
            "name": "Pevita Piss",
            "email": "pevita@safari.com",
            "phone": "+621234",
            "role": "Zookeeper",
            "schedule": "Mon-Sun, 8AM-4PM"
        },
        "2": {
            "id": "2",
            "name": "Bambang Kirun",
            "email": "bambangk@safari.com",
            "phone": "+6214321",
            "role": "Office Boy",
            "schedule": "Mon-Sun, 10AM-5PM"
        },
        "3": {
            "id": "3",
            "name": "Joko Mulyadi",
            "email": "Jokom@safari.com",
            "phone": "+6214433",
            "role": "Manager",
            "schedule": "Mon-Fri, 8AM-4PM"
        }
    }
}

animal_id_counter = len(database["animals"])
employee_id_counter = len(database["employees"])
