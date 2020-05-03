FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install catboost boto3 
COPY ./app /app
EXPOSE 8000
CMD ["uvicorn", "main:app"]