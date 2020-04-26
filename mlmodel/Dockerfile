# Yoinked from Python official Docker image

FROM python:3

WORKDIR /app

RUN pip install psycopg2-binary catboost scikit-learn numpy pandas

COPY . .
CMD [ "python", "./train.py" ]
