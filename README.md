# hbnb-2.0
remaster of my last hbnb

back-end -> fastAPI y clean architecture
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/postgresql-%23336791.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-e92063?style=for-the-badge&logo=pydantic&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

`como correr el backend`

* debes tener un .env (DATABASE_URL= SECRET_KEY= DEBUG=)

* debes moverte a la carpeta backend

* python3 -m venv venv

* pip install -r requirement.txt

* uvicorn app.main:app --reload

* "Una vez corriendo el servidor, puedes acceder a la documentación interactiva en http://localhost:8000/docs".

`comando para correr el software`

* docker compose up --build

`comando para remover la imagen de docker`

* docker compose down



`Estructura del project`

```
backend
    |- APP |
    |   |- API
    |   |   |- endpoint
    |   |   |   |- los endpoint para comunicar el software con el mundo exterior
    |   |   |- schemas
    |   |          |- modelos para enviar request y recibir responses
    |   |- DOMAIN
    |   |   |- MODELS
    |   |   |   |- modelos de las entidades involucradas
    |   |   |
    |   |   |- interfaces: es donde declaramos los metodos para el repo
    |   |
    |   |- INFRASTRUCTURE
    |   |       |- PERSISTENSE
    |   |       |       |-SQL ALCHEMY
    |   |       |       |   |- los repo que interactuan con la base de datos
    |   |       |       |
    |   |       |       |- database: session de database
    |   |       |       |- mem repository: repositorio en memoria (para posibles test)
    |   |       |       |- models: modelos de las tablas de la base de datos
    |   |       |- config
    |   |- USE CASES
    |   |   |- los use case representan las funcionalidades del software
    |   |
    |   |- main: archivo principal del software
    |
    |- test
    |- docker compose: levanta FastAPI y Postgre
    |- dockerfile: levanta la imagen de Python
```