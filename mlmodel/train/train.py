import numpy as np
import pandas as pd
import math
import config as creds
import psycopg2
import pickle
import boto3

import sklearn.metrics as metrics
from catboost import Pool, CatBoostRegressor
from sklearn.model_selection import RandomizedSearchCV, train_test_split

# Connect to RDS and retrieve training data
print("Opening connection to RDS...")
conn_string = "host="+creds.PGHOST+" port="+creds.PORT+" dbname="+creds.PGDATABASE+" user="+creds.PGUSER+" password="+creds.PGPASSWORD
conn = psycopg2.connect(conn_string)
cur = conn.cursor()
cur.execute('select * from houses')
data = pd.DataFrame(cur.fetchall())
cur.execute("""select column_name from information_schema.columns where table_name = 'houses'""")
columns = cur.fetchall()
c = []
for i in columns:
    c.append(i[0])
data.columns = c

# Use select features
print("Preparing data...")
data = data.loc[:,['suburb', 'rooms', 'type', 'price', 'postcode', 'bathroom', 'car']]
data = data.dropna()
X = data.drop(columns=["price"])
y = data["price"]

# Split data for training and evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
categorical = ['suburb', 'type', 'postcode']
train_pool = Pool(X_train, y_train, cat_features=categorical)
test_pool = Pool(X_test, cat_features=categorical)

# Find optimal hyper-parameters
print("Training model...")
model = CatBoostRegressor(loss_function="RMSE", logging_level=None)
grid = {'learning_rate': [0.01, 0.03, 0.06, 0.09, 0.12],
            'depth': [4, 6, 8, 10],
            'l2_leaf_reg': [1, 3, 5, 7, 9],
            'random_strength': [2, 4],
            'bagging_temperature': [0, 1],
        }
grid_search_result = model.randomized_search(grid, X=train_pool, search_by_train_test_split=True, verbose=False)

# Evaluate on test set
preds = model.predict(test_pool)

# Show metrics
print("Metrics")
print(metrics.mean_squared_error(y_test, preds))
print(metrics.mean_absolute_error(y_test, preds))
print(metrics.r2_score(y_test, preds))

# Save to file and S3 storage
pickle.dump(model, open("catboost.pkl", "wb"))
s3 = boto3.client("s3")
with open("catboost.pkl", "rb") as f:
    s3.upload_fileobj(f, "house-prediction-project", "mlmodel/catboost.pkl")
