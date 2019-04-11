#!/usr/bin/env python3

import datetime
import psycopg2

DBNAME = "news"

top_3_articles_query = """select articles.title, article_views.nb_views
 from articles join article_views on articles.slug = article_views.article
 order by article_views.nb_views desc
 limit 3;"""

most_popular_authors_query = """select name, sum(nb_views)::bigint as total_views
  from article_views a join authors_articles b on a.article=b.slug
   group by name order by total_views desc;"""

error_day_query = """select day, round(error_rate::numeric, 1)
 from daily_error_rate where error_rate > 1.0 order by error_rate desc;"""


def get_data(query):
    """Executes SQL query and returns results in a list of tuples."""
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def top_3_articles_report(query_result):
    intro = "Top 3 most popular articles:\n"
    with open('output.txt', mode='w') as f:
        f.write(intro)
        for entry in query_result:
            f.write(entry[0] + ' - ' + format(entry[1], ',d') + ' views\n')


def most_popular_authors_report(query_result):
    intro = "\nMost popular authors:"
    with open('output.txt', mode='a') as f:
        f.write(intro)
        for entry in query_result:
            f.write(
                '\n' + entry[0] + ' - ' + format(entry[1], ',d') + ' views'
                    )


def error_day_report(query_result):
    intro = "\n\nDays with more than 1 percent request errors:"
    with open('output.txt', mode='a') as f:
        f.write(intro)
        for entry in query_result:
            f.write(
                '\n' + entry[0].strftime("%d %B, %Y") +
                ' - ' + str(entry[1]) + ' % errors'
                    )


def main():
    print("Running reports...")
    top_3_articles_report(get_data(top_3_articles_query))
    most_popular_authors_report(get_data(most_popular_authors_query))
    error_day_report(get_data(error_day_query))
    print("Reports ready")


if __name__ == "__main__":
    main()
