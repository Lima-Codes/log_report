#!/usr/bin/env python3

import datetime
import psycopg2

DBNAME = "news"

top_3_articles_query = """select articles.title, article_views.nb_views
 from articles join article_views on articles.slug = article_views.article
 order by article_views.nb_views desc
 limit 3;"""

query = top_3_articles_query

def get_data(query):
  """Executes SQL query and returns results in a list of tuples."""
  conn = psycopg2.connect(database=DBNAME)
  cursor = conn.cursor()
  cursor.execute(query)
  results = cursor.fetchall()
  conn.close()

  return results

def top_3_articles_report(query_result):
  with open('output.txt', mode='w') as f:
    for entry in query_result:
      f.write(entry[0] + ' - ' + format(entry[1], ',d') + ' views\n')


if __name__ == "__main__":
  print(get_data(query))
  top_3_articles_report(get_data(query))