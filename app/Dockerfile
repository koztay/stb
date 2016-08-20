FROM python:3.5-onbuild
#FROM python:3.5
#ENV PYTHON UNBUFFERED 1
#ADD . /app
#WORKDIR "/app"
#RUN pip install -r requirements.txt
RUN SECRET_KEY=tmpkey python manage.py collectstatic --noinput
#
#CMD gunicorn ecommerce2.wsgi:application -b 0.0.0.0:8000