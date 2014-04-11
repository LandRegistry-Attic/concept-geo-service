FROM orchardup/python:2.7
RUN apt-get update -qq && apt-get install -qy python-psycopg2 binutils libproj-dev gdal-bin
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code
ENV PYTHONUNBUFFERED 1
