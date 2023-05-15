Title: Characterizing Database Workloads & Storage Models
Date: 2020-06-27 13:22
Author: pythonmarketer
Category: data, Databases, education, performance
Tags: Carnegie Mellon, database storage, learning, lectures notes
Slug: choosing-database-storage-models-and-workloads-that-mesh
Status: published

Thank you [Carnegie Mellon Database Group](https://db.cs.cmu.edu/) for putting this online! These are my notes from watching on YouTube.

> Carnegie Mellon Databases Storage II, Lecture 4
>
> Prof. Andy Pavlo \[[Watch on YouTube](https://www.youtube.com/watch?v=YWRYEXNy6IE&list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi&index=4)\]

## The Problem and Solution

How should the DBMS represent the database in storage files on disk? Solve it by choosing the right *storage model* for your target *workload*. The right strategy varies if you are reading data, writing data and with how many joins you are performing.

## Workload Characterization

**OLTP** ([Online Transaction Processing](https://en.wikipedia.org/wiki/Online_transaction_processing)): "Simple queries with lots of writes."

**OLAP** ([Online Analytical Processing](https://en.wikipedia.org/wiki/Online_analytical_processing)): "Read only queries. Lots of joins. Doing a lot of reads, but they're more complex."

**HTAP** ([Hybrid Transactional Analytical Processing](https://en.wikipedia.org/wiki/Hybrid_transactional/analytical_processing)): "is trying to do both of them. You still want to ingest new data, but analyze it as it comes in. It's used for companies making decisions on the fly as people are browsing websites, like internet advertising companies."

## ![Screenshot 2020-06-27 at 11.56.10 AM](https://pythonmarketer.files.wordpress.com/2020/06/screenshot-2020-06-27-at-11.56.10-am.png){.alignnone .size-full .wp-image-3897 width="1920" height="1080"}

## Storage Models

*screenshots from the [lecture](https://www.youtube.com/watch?v=YWRYEXNy6IE&list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi&index=4)*

![n-ary model](https://pythonmarketer.files.wordpress.com/2020/06/n-ary-model.png){.alignnone .size-full .wp-image-3918 width="692" height="360"}

N-ary used to be the dominant model until the '80s.

![DSM model](https://pythonmarketer.files.wordpress.com/2020/06/dsm-model-1.png){.alignnone .size-full .wp-image-3917 width="938" height="396"}

**Additional Reading:** [All Things Distributed](https://www.allthingsdistributed.com/2013/09/column-oriented-databases.html)

## Column Store Vs. Row Store RDBMS

**[Row-oriented DBMS](https://dataschool.com/data-modeling-101/row-vs-column-oriented-databases/) (Row Store)**

-   PostgreSQL, MySQL
-   Row Store = use OLTP

**[Column-oriented DBMS](https://en.wikipedia.org/wiki/Column-oriented_DBMS) (Column Store)**

-   Red Shift, BigQuery
-   Column Store = use OLAP

If types are consistent, you can compress data into single column store.
