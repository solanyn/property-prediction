FROM python:3

WORKDIR /usr/src/app

RUN pip install psycopg2-binary catboost scikit-learn numpy pandas

COPY . .
CMD [ "python", "./train.py" ]

RUN echo "Model saved to file!"