psql \ # [1]
   --host=mltrainingdb.ci2ii1wmuvpx.us-east-1.rds.amazonaws.com \
   --port=5432 \
   --username=postgres \
   --password \
   --dbname=mltrainingdb \
   -f create_table.sql
# Enter password when prompted


# Reference:
# [1]"PostgreSQL 11.8 Documentation", postgresql.org, 2020. [Online]. Available: https://www.postgresql.org/docs/11/index.html. [Accessed: 07- May- 2020].
