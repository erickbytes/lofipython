Title: Pondering Join Algorithms
Date: 2020-08-09 18:24
Author: pythonmarketer
Category: coding, data, Databases, programming
Tags: algorithms, computer science, joins, learning, study, technology
Slug: join-algorithms
Status: published

Truly enjoying this [**Intro to Database Systems** course](https://www.youtube.com/playlist?list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi) from Carnegie Mellon University. Some really great breakdowns of common join algorithms in this lecture. Here are my notes.

> **[Lecture 11- Join Algorithms](https://www.youtube.com/watch?v=nUwT7PEQ49o&list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi&index=11) (CMU Databases Systems / Fall 2019)**
>
> Prof. Andy Pavlo, Carnegie Mellon Database Group

![Join Algorithms](https://pythonmarketer.files.wordpress.com/2020/08/join-algorithms.png){.alignnone .size-full .wp-image-4118 width="747" height="404"}

*screenshot from lecture*

**Table Positioning for a Join**

"In general, your smaller table should be the "left" table when joining two tables."... Professor demonstrates better performance by making the smaller table the "outer" table in a join.

**Block Nested Loop Join \[[mysql example](https://dev.mysql.com/doc/refman/5.7/en/nested-loop-joins.html#:~:text=A%20Block%20Nested%2DLoop%20(BNL,inner%20loops%20must%20be%20read.&text=The%20join_buffer_size%20system%20variable%20determines,used%20to%20process%20a%20query.)\]**

-   "The brute force approach"
-   If you have enough memory to hold a large table, a good option for joining.
-   Always pick the smaller table as the outer table.
-   Buffer as much of your outer table in memory as possible to reduce redundant I/O.
-   Loop over the inner table or use an index.

**Index Nested Loop Join \[[CS Course definition](https://www.cs.carleton.edu/faculty/dmusicant/cs347f03/proj3/)\]**

If indexes are available, or you could create an index to use for a join.

**Sort-Merge Join \[[wikipedia](https://en.wikipedia.org/wiki/Sort-merge_join)\]**

Useful if one or both tables are sorted on a join key. Maximize sequential I/O.

![Sort - Merge Join](https://pythonmarketer.files.wordpress.com/2020/08/sort-merge-join-1.png){.alignnone .size-full .wp-image-4121 width="1731" height="855"}

*screenshot from lecture*

**Hash Join \[[mysql blog example](https://mysqlserverteam.com/hash-join-in-mysql-8/#:~:text=Hash%20join%20is%20a%20way,inputs%20can%20fit%20in%20memory.)\]**

Best performance. For large datasets.

1.  Phase #1 Build (Hash Table)
2.  Phase #2 Probe

**Use [Bloom Filter](https://en.wikipedia.org/wiki/Bloom_filter) set operations for probe phase optimization**

1.  insert a key
2.  lookup a key

> **Additional Reading on Bloom Filters**
>
> [Let's implement a Bloom Filter](https://onatm.dev/2020/08/10/let-s-implement-a-bloom-filter/)
>
> [Bloom Filters Debunked](https://gopiandcode.uk/logs/log-bloomfilters-debunked.html)

**Grace Hash Join** \[[wikipedia](https://en.wikipedia.org/wiki/Hash_join#Grace_hash_join)\]

-   "Do hash joins when things don't fit in memory."
-   Use a hash table for each table. Break the tables into buckets then do a nested loop join on each bucket. If the buckets do not fit in memory, use [recursive partitioning](https://en.wikipedia.org/wiki/Recursive_partitioning#:~:text=Recursive%20partitioning%20is%20a%20statistical,on%20several%20dichotomous%20independent%20variables.). Then everything fits in memory for the join.

> "Split outer relation into partitions based on the hash key."
>
> Prof. Andy Pavlo on Hash Join algorithm

-   Hashing is almost always better than sorting for operator execution.

> "No join algorithm works well in all scenarios."
>
> -Prof. Andy Pavlo
