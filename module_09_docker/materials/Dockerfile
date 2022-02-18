FROM python:3.7.9-slim-stretch

RUN mkdir /apps

COPY new_year_application/ apps/

RUN python -m pip install -r apps/requirements.txt

WORKDIR /apps

ENTRYPOINT ["python", "app.py"]



