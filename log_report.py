#!/usr/bin/env python3

import datetime
import psycopg2

DBNAME = "news"
query = "select * from authors;"

def get_data(query):
  """Executes SQL query and returns results in a list of tuples."""
  conn = psycopg2.connect(database=DBNAME)
  cursor = conn.cursor()
  cursor.execute(query)
  results = cursor.fetchall()
  conn.close()

  return results


if __name__ == "__main__":
  print(get_data(query))