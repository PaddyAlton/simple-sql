# create_database.py

# the intention is to be as lightweight as possible; to prove it's easy
# rather than to write well-structured code with dependency management.
# So: you'll need to install pandas and sqlalchemy to make this work.

from pandas import DataFrame
from sqlalchemy import create_engine


if __name__ == "__main__":

    database_location = "db.sqlite"  # any valid file path

    connection_string = f"sqlite:///{database_location}"  # use SQLite driver, file is the database

    engine = create_engine(connection_string)  # SQL engine

    table_name = "people"  # table we'll write the data to

    data = DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})  # data we'll write to it

    data.to_sql(table_name, engine, if_exists="replace")  # recreate if need be
