# hbnb-2.0
remaster of my last hbnb

back-end -> fastAPI y clean architecture

dia 1 -> configurar estructura de carpetas (Clean Architecture) y archivos base

`como correr el backend`

* debes tener un .env (DATABASE_URL= SECRET_KEY= DEBUG=)

* debes moverte a la carpeta backend

* python3 -m venv venv

* pip install requirement.txt

* uvicorn app.main:app --reload

* "Una vez corriendo el servidor, puedes acceder a la documentación interactiva en http://localhost:8000/docs".

`comando para correr el software`

* docker compose up --build

`comando para remover la imagen de docker`

* docker compose down



`Estructura del project`

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
