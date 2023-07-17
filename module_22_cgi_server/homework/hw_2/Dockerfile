FROM python:3.7.9-slim-stretch
FROM nginx

WORKDIR /app


RUN apt-get update && apt-get upgrade -y && apt-get install -y python3-pip supervisor nginx && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/
COPY routes.py /app/


RUN python3 -m pip install -r requirements.txt --break-system-packages


COPY ./static /app/static
COPY ./templates /app/templates
COPY nginx.conf /etc/nginx/nginx.conf
COPY uwsgi.ini /etc/uwsgi/uwsgi.ini
COPY supervisord.ini /etc/supervisor/conf.d/supervisord.ini



CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.ini"]
CMD ["systemctl", "nginx", "restart"]
CMD ["uwsgi", "--ini mywsgi.ini"]
CMD ["python3", "routes.py"]

