# Log Analysis Project
This Python program is a reporting tool that prints out reports (in plain text) based on data in the 'news' database. It uses the psycopg2 module to connect to the database.  

* * *

## Program Output

This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

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

## Usage
To get this program up and running, you will need to do the following:


### Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

### Download the VM configuration
There are a couple of different ways you can download the VM configuration.

You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

### Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM.

### Create views
In your vagrant VM, change directory using `cd /vagrant` then run the command `psql`. Create the views using the SQL statements in the [Views](#views) section.

### Run the program
In your vagrant VM, run `python log_report.py` to generate the report.

## Views
The following views were created and are used for easier SQL queries:

1. **article_views**

~~~~sql
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
~~~~

2. **authors_articles**

~~~~sql
CREATE VIEW authors_articles AS
SELECT
    authors.name,
    articles.slug
FROM
    articles
    JOIN authors ON articles.author = authors.id;
~~~~

3. **daily_error_rate**

~~~~sql
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
~~~~


