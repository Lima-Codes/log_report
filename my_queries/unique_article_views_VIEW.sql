CREATE VIEW unique_article_views AS
SELECT
    split_part(
        path, '/', 3) AS article,
    count (
        distinct ip) AS unique_nb_views
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
    unique_nb_views DESC
