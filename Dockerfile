FROM ubuntu:18.04

LABEL maintainer="yannick.feler@gmail.com"

ENV LC_ALL C.UTF-8

ENV LANG C.UTF-8

RUN apt-get update -y && \
    apt-get install -y python3 python3-all-dev python3-pip build-essential swig git libpulse-dev libasound2-dev

# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "bash" ]
EXPOSE 5000

CMD [ "run.sh" ]

