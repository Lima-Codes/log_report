# Log Analysis Project
This Python program is a reporting tool that prints out reports (in plain text) based on  data in the 'news' database. It uses the psycopg2 module to connect to the database.  

* * *

## Program Output

The program generates 3 reports answering the following questions:

1. **What are the most popular three articles of all time?** Which articles have been accessed the most? Presented as a sorted list with the most popular article at the top.

    Example:  
    + "Princess Shellfish Marries Prince Handsome" — 1201 views
    + "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
    + "Political Scandal Ends In Political Scandal" — 553 views


2. **Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Presented as a sorted list with the most popular author at the top.

    Example:  
    + Ursula La Multa — 2304 views
    + Rudolf von Treppenwitz — 1985 views
    + Markoff Chaney — 1723 views
    + Anonymous Contributor — 1023 views


3. **On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

    Example:  
    + July 29, 2016 — 2.5% errors

## Views used
The following views were created and are used for easier SQL queries:

1. **article_views**

`CREATE VIEW article_views AS
SELECT
    split_part(
        path, '/', 3) AS article,
    count(
        *) AS nb_views
FROM
    log
WHERE
    method = 'GET'
    AND status = '200 OK'
    AND length(split_part (
        path, '/', 3)) > 0
GROUP BY
    article
ORDER BY
    nb_views DESC;`

2. **authors_articles**

`CREATE VIEW authors_articles AS
SELECT
    authors.name,
    articles.slug
FROM
    articles
    JOIN authors ON articles.author = authors.id;`


