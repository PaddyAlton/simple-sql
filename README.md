simple-sql
==========

A quick demonstration of using python to set up and query data from a SQLite database.

The intention is to make this as simple as possible, so I haven't got tests, dependency management etc.

To make it work:

- make sure you have `pandas` and `sqlalchemy` installed: `pip install pandas sqlalchemy --upgrade`
- `python create_database.py` will (re-)create a SQLite database file (`db.sqlite`)
- `python read_database.py` will query the database and display a DataFrame containing the output
