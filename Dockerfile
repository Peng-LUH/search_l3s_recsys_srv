FROM python:3.9slim

WORKDIR /code
COPY . /code

RUN apt-get update
RUN apt-get -y install python3-dev

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN pip install -e .

CMD [ "flask", "run", "--port=9042", "--host=0.0.0.0"]

EXPOSE 9042

