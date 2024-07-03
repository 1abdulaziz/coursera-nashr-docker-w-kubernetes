# Commands
- export FLASK_APP=project/__init__.py
- export FLASK_RUN_PORT=5001
- to build the image run `docker-compose up -d --build`
- run `docker-compose exec web python manage.py create
_db`
- `\l` list databases
- `\c <database-name>`
- `\dt` list tables
- `\q` 
- sheck if volume is exsist `docker volume inspect flask-on-docker_postgres_data`
# ERROR

- IF YOU HAVE ANY ERROR DELETE ALL IMAGES AND RUN `docker-compose up -d --build`