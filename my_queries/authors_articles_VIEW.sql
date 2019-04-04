CREATE VIEW authors_articles AS
SELECT
    authors.name,
    articles.slug
FROM
    articles
    JOIN authors ON articles.author = authors.id;
