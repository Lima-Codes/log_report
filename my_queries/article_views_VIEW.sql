CREATE VIEW article_views AS
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
    nb_views DESC;

