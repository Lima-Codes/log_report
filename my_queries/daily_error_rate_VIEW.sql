CREATE VIEW daily_error_rate AS
SELECT
    *,
    (
        b.nb_errors * 100.0 / a.nb_requests)::float AS error_rate
FROM (
    SELECT
        time::date AS day,
        count(status) AS nb_requests
    FROM
        log
    GROUP BY
        time::date) a
    JOIN (
        SELECT
            time::date AS day_2,
            count(status) AS nb_errors
        FROM
            log
        WHERE
            status LIKE '%404%'
        GROUP BY
            time::date) b ON a.day = b.day_2
ORDER BY
    a.day DESC;

