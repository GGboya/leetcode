FROM python:3.7

WORKDIR ./http

ADD . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./main.py"]