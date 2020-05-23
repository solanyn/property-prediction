# Amazon RDS set up

The directory contains a single shell script which inserts the data the CSV file into the PostgreSQL RDS database instance.

Before running, please make sure the training data `Melbourne_housing_FULL.csv` is included in the directory from Melbourne Housing Market on Kaggle[1]. 

Make `psql.sh` executable by running:

`sudo chmod +x psql.sh`

Then run it by using:

`./psql.sh`

Enter password to the RDS instance when prompted.

## References
[1]A. Pino, "Melbourne Housing Market", kaggle.com, 2020. [Online]. Available: https://www.kaggle.com/anthonypino/melbourne-housing-market. [Accessed: 07- May- 2020].
