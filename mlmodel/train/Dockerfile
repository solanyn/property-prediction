FROM python:3

RUN pip install scikit-learn catboost psycopg2-binary boto3 

WORKDIR /app

COPY ./train.py /app
COPY ./config.py /app

CMD ["python", "/app/train.py"
