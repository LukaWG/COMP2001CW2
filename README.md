# COMP2001 CW2 | Trail Service MicroService
This microservice provides an API for managing trails, locations, features, and their relationships. It has been built using Flask, SQLAlchemy, and Marshmallow, and it uses a Microsoft SQL Server for the database.

## Features

- Authentication
    - Role based access is provided for creating, updating, and deleting trails
- Trail Management
    - All CRUD procedures have been implemented for trails
- Database integration
    - The API has been linked to a Microsoft SQL Server database to store trail data

## External Modules Required
- Flask
- Connexion
- SQLAlchemy
- Marshmallow

## Setup and Running Option 1
### 1. Clone the Repository
```cmd
git clone https://github.com/LukaWG/COMP2001CW2.git
cd ./COMP2001CW2
```

### 2. Setup Virtual Environment
```cmd
conda create --name <Environment Name> python=3.10
conda activate <Environment Name>
```
Note: To deactivate virtual environment run ```conda deactivate```

### 3. Install Requirements
```cmd
pip install -r requirements.txt
```
### 4. Setup Database Connection
- In ```config.py``` update the database connection details for your database

### 5. Run
```cmd
python ./app.py
```

### Swagger UI
- View the API Swagger documentation by going to <a href="localhost:8000/api/ui">localhost:8000/api/ui</a>

## Setup and Running Option 2
### Docker
1. Make sure Docker is running
2. Pull Docker container
```cmd
docker pull lukawg/comp2001cw2
```
3. Run Docker container
```cmd
docker run -p 8000:8000 lukawg/comp2001cw2
```
4. Connect to API Swagger documentation on <a href="localhost:8000/api/ui">localhost:8000/api/ui</a>