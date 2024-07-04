FROM python:3.11.3-slim-buster

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app

RUN apt-get update && apt-get install -y netcat
ENTRYPOINT [ "sh", "./usr/src/app/entrypoint.sh" ]
CMD [ "python", "manage.py", "run" , "--host=0.0.0.0"]