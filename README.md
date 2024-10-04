# Zoo Management System

Welcome to the **Safari Zoo Management System**! This is a simple web-based application built with Flask to manage information about animals and employees at the zoo.
Deployed on koyeb (https://interesting-robby-fans-ard-338584a9.koyeb.app/)

## Features

- **Animal Management**: Add, view, update, and delete animal information.
- **Employee Management**: Add, view, update, and delete employee information.
- **API Documentation**: Uses **Swagger** for API documentation.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.11.x
- [Poetry](https://python-poetry.org/) for dependency management
- Docker (optional, to run the app in a container)

## Local Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/revou-fsse-5/module-6-FabianusArdian.git
    ```

2. Activate the virtual environment using **Poetry**:

    ```bash
    poetry install
    poetry shell
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Access the application in your browser:

    - **Home Page**: [http://localhost:5000/](http://localhost:5000/)
    - **Swagger API Documentation**: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)


### Animal Management

- **GET /animals**: Get a list of all animals.
- **GET /animals/{id}**: Get details of a specific animal by ID.
- **POST /animals**: Add a new animal (requires JSON format).
- **PUT /animals/{id}**: Update an existing animal by ID.
- **DELETE /animals/{id}**: Delete an animal by ID.

### Employee Management

- **GET /employees**: Get a list of all employees.
- **GET /employees/{id}**: Get details of a specific employee by ID.
- **POST /employees**: Add a new employee (requires JSON format).
- **PUT /employees/{id}**: Update an existing employee by ID.
- **DELETE /employees/{id}**: Delete an employee by ID.

