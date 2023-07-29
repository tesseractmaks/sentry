FROM python:3.7.9-slim-stretch
FROM sentry:latest


WORKDIR /app

COPY task_1.py /app/

RUN pip install flask
RUN pip install --upgrade 'sentry-sdk[flask]'
RUN apt-get -y install git


#CMD ["python", "task_1.py"]