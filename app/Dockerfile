FROM python:3.5.2
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

RUN SECRET_KEY=tmpkey python manage.py collectstatic --noinput


