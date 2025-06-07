# Fetch-FlaskWebService
Receipt Processor Take Home Challenge

### Entrypoint to Flask Application 
- app/__init__.py -> create_app()

### Running the APP
- PYTHONPATH=. flask --app app --debug run

### Running tests -> Navigate to app/tests
- PYTHONPATH=. pytest

### API Docs
- http://127.0.0.1:5000/apidoc/swagger
- http://127.0.0.1:5000/apidoc/redoc 

### APPLICATION STRUCTURE
##### Layers
- DTO -> Should Validate Data w/ Pydantic
- Model -> Business Logic
- Service Layer -> Interfaces with models and Repository to perform tasks
- Repo -> Interfaces with the database to perform operations in a functional manner 
- DB -> In memory ORM mock client. 

### Docker Build -> Naviagte to project home (one folder outside of app)
docker build -t fetch-flask-app .

### Docker Run 
docker run -p 5001:5001 fetch-flask-app
Go to the following link: http://127.0.0.1:5001/ 

### Run tests using Docker 
docker run --rm fetch-flask-app pytest app/tests/
