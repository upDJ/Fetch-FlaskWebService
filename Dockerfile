FROM python:slim

WORKDIR /fetch_project

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app

EXPOSE 5001

ENV FLASK_APP=app:create_app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001
ENV PYTHONPATH=.

CMD ["flask", "run"]