Characterizing Database Workloads & Storage Models
##################################################
:date: 2020-06-27 13:22
:author: pythonmarketer
:category: data, Databases, education, performance
:tags: Carnegie Mellon, database storage, learning, lectures notes
:slug: choosing-database-storage-models-and-workloads-that-mesh
:status: published

Thank you `Carnegie Mellon Database Group <https://db.cs.cmu.edu/>`__ for putting this online! These are my notes from watching on YouTube.

   Carnegie Mellon Databases Storage II, Lecture 4

   Prof. Andy Pavlo [`Watch on YouTube <https://www.youtube.com/watch?v=YWRYEXNy6IE&list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi&index=4>`__]

The Problem and Solution
------------------------

How should the DBMS represent the database in storage files on disk? Solve it by choosing the right *storage model* for your target *workload*. The right strategy varies if you are reading data, writing data and with how many joins you are performing.

Workload Characterization
-------------------------

**OLTP** (`Online Transaction Processing <https://en.wikipedia.org/wiki/Online_transaction_processing>`__): "Simple queries with lots of writes."

**OLAP** (`Online Analytical Processing <https://en.wikipedia.org/wiki/Online_analytical_processing>`__): "Read only queries. Lots of joins. Doing a lot of reads, but they're more complex."

**HTAP** (`Hybrid Transactional Analytical Processing <https://en.wikipedia.org/wiki/Hybrid_transactional/analytical_processing>`__): "is trying to do both of them. You still want to ingest new data, but analyze it as it comes in. It's used for companies making decisions on the fly as people are browsing websites, like internet advertising companies."

|Screenshot 2020-06-27 at 11.56.10 AM|
--------------------------------------

Storage Models
--------------

*screenshots from the*\ `lecture <https://www.youtube.com/watch?v=YWRYEXNy6IE&list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi&index=4>`__

.. image:: https://pythonmarketer.files.wordpress.com/2020/06/n-ary-model.png
   :alt: n-ary model
   :class: alignnone size-full wp-image-3918
   :width: 692px
   :height: 360px

N-ary used to be the dominant model until the '80s.

.. image:: https://pythonmarketer.files.wordpress.com/2020/06/dsm-model-1.png
   :alt: DSM model
   :class: alignnone size-full wp-image-3917
   :width: 938px
   :height: 396px

**Additional Reading:** `All Things Distributed <https://www.allthingsdistributed.com/2013/09/column-oriented-databases.html>`__

Column Store Vs. Row Store RDBMS
--------------------------------

`Row-oriented DBMS <https://dataschool.com/data-modeling-101/row-vs-column-oriented-databases/>`__\ **(Row Store)**

-  PostgreSQL, MySQL
-  Row Store = use OLTP

`Column-oriented DBMS <https://en.wikipedia.org/wiki/Column-oriented_DBMS>`__\ **(Column Store)**

-  Red Shift, BigQuery
-  Column Store = use OLAP

If types are consistent, you can compress data into single column store.

.. |Screenshot 2020-06-27 at 11.56.10 AM| image:: https://pythonmarketer.files.wordpress.com/2020/06/screenshot-2020-06-27-at-11.56.10-am.png
   :class: alignnone size-full wp-image-3897
   :width: 1920px
   :height: 1080px
