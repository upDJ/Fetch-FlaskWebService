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
- Repo -> 
