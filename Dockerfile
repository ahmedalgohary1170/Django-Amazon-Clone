# start docker kernal + python

FROM python:3.11.9-slim-bullseye
# show logs : python
ENV PYTHONUNBUFFERED = 1

#update kernal + install
RUN apt-get update && apt-get -y install gcc libpq-dev

# folder for my project
WORKDIR /app

# copy requirments
COPY requirments.txt /app/requirments.txt

# install requirments
RUN pip install -r /app/requirments.txt

# copy all project file
COPY . /app/