FROM python:3.7.9-slim-stretch
FROM sentry:latest

WORKDIR /app

COPY task_1.py /app/

RUN pip install flask
RUN pip install --upgrade 'sentry-sdk[flask]'

#CMD ["python", "task_1.py"]