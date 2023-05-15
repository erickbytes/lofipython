Title: Memory Monitoring Python Libraries + Tools
Date: 2021-12-19 11:57
Author: pythonmarketer
Category: coding, computing, pandas, performance, programming
Tags: memory profiling, monitoring, python, RAM, Windows
Slug: tools-tips-to-beat-memoryerror-in-your-python-scripts
Status: published

`<!-- wp:paragraph -->`{=html}

If you write Python code, there's probably been a time or two when you saw the dreaded ["MemoryError"](https://docs.python.org/3/library/exceptions.html#MemoryError). This happens after one of your Python scripts stops because your computer has no spare [RAM](https://en.wikipedia.org/wiki/Random-access_memory) to execute it. I recently experienced this frustration whilst trying to write hundreds of thousands of csv files. However, this time I grasped for tools that support smarter memory management. Now, I can watch my computer's memory bounce around with the Windows Resource Monitor. Python has quite a few memory profiling libraries for monitoring memory too!

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Python Libraries and Guides**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Memory Management Overview](https://docs.python.org/3/c-api/memory.html), Python documentation

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Memory Profiler](https://github.com/pythonprofilers/memory_profiler): "monitor memory usage of Python code"

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[psutil](https://github.com/giampaolo/psutil): "Cross-platform lib for process and system monitoring in Python"

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[py-spy](https://github.com/benfred/py-spy): "Sampling profiler for Python programs"

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[pyinstrument](https://github.com/joerick/pyinstrument): "🚴 Call stack profiler for Python. Shows you why your code is slow!"

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Scalene](https://github.com/plasma-umass/scalene): "a high-performance, high-precision CPU, GPU, and memory profiler for Python"

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[G](https://github.com/nicolargo/glances)[lances](https://github.com/nicolargo/glances): "Glances an Eye on your system. A top/htop alternative for GNU/Linux, BSD, Mac OS and Windows operating systems."

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Yappi](https://github.com/sumerc/yappi): "Yet Another Python Profiler, but this time thread&coroutine&greenlet aware."

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Fil](https://github.com/pythonspeed/filprofiler): "A Python memory profiler for data processing and scientific computing applications" ([Video](https://www.youtube.com/watch?v=2nKvzVIUjLE&ab_channel=PyninsulaOfficial))

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[line_profiler](https://github.com/pyutils/line_profiler): "Line-by-line profiling for Python"

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[pprofile](https://github.com/vpelletier/pprofile): "Line-granularity, thread-aware deterministic and statistic pure-python profiler"

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Guppy 3](https://github.com/zhuyifei1999/guppy3/): "Python programming environment and heap analysis toolset"

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

S*ee also:* [The Python Profilers](https://docs.python.org/3/library/profile.html), Python documentation

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:quote -->`{=html}

> `<!-- wp:paragraph -->`{=html}
>
> CPython standard distribution comes with three deterministic profilers. `cProfile`, `Profile` and `hotshot`. `cProfile` is implemented as a C module based on `lsprof`, `Profile` is in pure Python and `hotshot` can be seen as a small subset of a cProfile.
>
> `<!-- /wp:paragraph -->`{=html}`<cite>`{=html}Yappi Github, <https://github.com/sumerc/yappi>`</cite>`{=html}

`<!-- /wp:quote -->`{=html}

`<!-- wp:paragraph -->`{=html}

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Windows** **Tools**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Task Manager](https://en.wikipedia.org/wiki/Windows_Task_Manager#:~:text=The%20program%20can%20be%20started,typing%20taskmgr%20in%20the%20File): Windows process management tool with some memory analytics

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Collect Data in Windows with Performance Monitor](https://help.tableau.com/current/server/en-us/perf_collect_perfmon.htm)

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

[Resource Monitor](https://en.wikipedia.org/wiki/Resource_Monitor): Windows tool with Memory, CPU, Disk and Network monitoring tabs

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:image {"align":"center","id":6300,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![Resource Monitor can stop processes from running and view in use, standby (Cached) and free memory. This shows 7 Python scripts running and 49% of total memory is being consumed. Looks like we are running steady and safely below "MemoryError" overflow. We might be able to add a few more scripts with 51% of RAM available!](https://pythonmarketer.files.wordpress.com/2021/12/resource-monitor-labels-full.jpg?w=796){.wp-image-6300}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Memory Tips and Guides**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list -->`{=html}

-   [Memory Management in Python](https://towardsdatascience.com/memory-management-in-python-6bea0c8aecc9), Towards Data Science: this article shows some memory efficient ways to write your code.
-   Use only the data you need. Any data you read in and aren't using is held in memory. The [usecols argument](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) in pandas is a great way to read a csv and only use the columns you need.
-   [Reading data in chunks](https://pythonspeed.com/articles/chunking-pandas/) with the [chunksize argument](https://github.com/pandas-dev/pandas/blob/v1.3.5/pandas/io/parsers/readers.py#L491-L586) is another way to reduce memory usage for large datasets.
-   [Measuring the memory usage of a Pandas dataframe](https://pythonspeed.com/articles/pandas-dataframe-series-memory-usage/)
-   Some tools are line oriented, others are function oriented. If your code contains large functions, you might favor a line based profiling tool.
-   Be aware of the overhead some memory tools may incur. memory_profile was clocked with a whopping 270x slowdown per the Scalene PyCon talk below. The talk shows an awesome comparison of these Python profiling libraries:

`<!-- /wp:list -->`{=html}

`<!-- wp:image {"id":6330,"sizeSlug":"large","linkDestination":"none"} -->`{=html}

![](https://pythonmarketer.files.wordpress.com/2021/12/scalene-pycon-us-2021-memory-library-comparison.png?w=1024){.wp-image-6330}

`<!-- /wp:image -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Recommended Reading**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:list -->`{=html}

-   [Profiling and Analyzing Performance of Python Programs](https://martinheinz.dev/blog/64)
-   [profile, cProfile, and pstats – Performance analysis of Python programs.](http://pymotw.com/2/profile/)
-   [Profiling and Analyzing Performance of Python Programs](https://martinheinz.dev/blog/64)
-   [20 Linux Memory Management Command Line Tools](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)
-   [Random-access Memory (RAM)](https://en.wikipedia.org/wiki/Random-access_memory)
-   [Cache Memory](https://computersciencewiki.org/index.php/Cache_memory)

`<!-- /wp:list -->`{=html}

`<!-- wp:paragraph -->`{=html}

**Conclusion**

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

When you'll see "MemoryError" depends on your computer's hardware, the size of your dataset and what operations you need to script out. Generally speaking, [I/O](https://en.wikipedia.org/wiki/Input/output) or file reads and writes are more expensive operations.

`<!-- /wp:paragraph -->`{=html}

`<!-- wp:paragraph -->`{=html}

The tools in this post will help you anticipate how much computing power you have available, monitor your memory consumption more closely and avoid pushing your computer past its limits. You can do things like reading data in chunks and only using the columns you need to reduce your memory consumption. Realizing these tools and strategies can make getting things done with Python a smoother ride.

`<!-- /wp:paragraph -->`{=html}
