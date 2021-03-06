# read_database.py
# executes a SQL query and prints the output

import pandas as pd

from sqlalchemy import create_engine


if __name__ == "__main__":

    database_location = "db.sqlite"  # any valid file path

    connection_string = f"sqlite:///{database_location}"  # use SQLite driver, file is the database

    engine = create_engine(connection_string)  # SQL engine

    query = "SELECT id, name FROM people WHERE name <> 'Alice';"  # SQL query to make

    data = pd.read_sql(query, engine, index_col="id")  # retrieve data from database file

    print(data)  # display the output
