import sqlalchemy
import psycopg2
import os

db_params = {
    "dbname": os.getenv("PG_DATABASE"),
    "user": os.getenv("PG_USER"),
    "password": os.getenv("PG_PASSWORD"),
    "host": os.getenv("PG_HOST"),
    "port": os.getenv("PG_PORT"),
}


def create_database(dbname):
    try:
        conn = psycopg2.connect(
            dbname=db_params["dbname"],
            user=db_params["user"],
            password=db_params["password"],
            host=db_params["host"],
        )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {dbname}")
        cursor.close()
        conn.close()
        print(f"Database {db_params["dbname"]} created successfully.")
    except Exception as e:
        print(f"Failed to create database: {e}")

def db_connection():
    return sqlalchemy.create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}')


# create_database(db_params["dbname"])

# engine = sqlalchemy.create_engine(
#     # "postgresql+psycopg2:///filipe:mysecretword123@localhost/nobel_winners", echo=True
#     f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}'
# )

