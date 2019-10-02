
-- CREATE DATABASE `scraping` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;

use scraping;

-- drop table google_search;

create table google_search (
id int auto_increment primary key,
keyword varchar(100),
url varchar(1000),
is_excluded bit default 0,
is_run bit default 0,
created timestamp
);

-- create table google_search_bk as select * from google_search;

-- truncate table google_search;

select * from google_search;
