import numpy as np
import pandas as pd
import math
import config as creds
import psycopg2

import sklearn.metrics as metrics
from catboost import Pool, CatBoostRegressor
from sklearn.model_selection import RandomizedSearchCV, train_test_split

# Connect to RDS and retrieve training data
print("Opening connection to RDS...")
conn_string = "host="+creds.PGHOST+" port="+creds.PORT+" dbname="+creds.PGDATABASE+" user="+creds.PGUSER+" password="+creds.PGPASSWORD
conn = psycopg2.connect(conn_string)
cur = conn.cursor()
cur.execute('select * from houses')

# Use select features
print("Preparing data...")
data = pd.DataFrame(cur.fetchall())
data = data.loc[:,['suburb', 'rooms', 'type', 'price', 'postcode', 'bathroom', 'car', 'landsize', 'councilarea', 'regionname']]
data = data.dropna()
X = data.drop(columns=["price"])
y = data["price"]

# Split data for training and evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
categorical = ['suburb', 'type', 'postcode', 'councilarea', 'regionname']
train_pool = Pool(X_train, y_train, cat_features=categorical)
test_pool = Pool(X_test, cat_features=categorical)

# Find optimal hyper-parameters
print("Training model...")
model = CatBoostRegressor(loss_function="RMSE")
grid = {'learning_rate': [0.01, 0.03, 0.06, 0.09, 0.12],
            'depth': [4, 6, 8, 10],
            'l2_leaf_reg': [1, 3, 5, 7, 9],
            'random_strength': [2, 4],
            'bagging_temperature': [0, 1],
        }
grid_search_result = model.randomized_search(grid, X=train_pool, plot=True, search_by_train_test_split=True)

# Evaluate on test set
preds = model.predict(test_pool)

# Show metrics
print("Metrics")
print(metrics.mean_squared_error(y_test, preds))
print(metrics.mean_absolute_error(y_test, preds))
print(metrics.r2_score(y_test, preds))

catboost.save_model(model, "catboost.model")