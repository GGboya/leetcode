FROM python:3.7

WORKDIR ./http

ADD . .

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ENTRYPOINT ["python", "./main.py"]