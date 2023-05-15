Benefits of Go and Threads in Distributed Systems
#################################################
:date: 2020-07-15 00:24
:author: pythonmarketer
:category: coding, concurrency, data, education, Go, lectures notes, programming
:tags: computers, distributed systems, golang, MIT, python, rpc
:slug: benefits-of-go-and-threads-in-distributed-systems
:status: published

**Preface**

These are my `YouTube lecture <https://www.youtube.com/watch?v=gA4YXUJX7t8&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB&index=3&t=0s>`__ notes from MIT's Distributed Systems course. Thank you MIT and Professor Morris!

   `MIT 6.824 Distributed Systems <https://www.youtube.com/playlist?list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB>`__

   Lecture 2: RPC and Threads - Feb 7, 2020

   Prof. Robert Morris (Spring 2020)

**Introduction**

Go is a popular programming language choice so my ears perked up when this lecture began. These notes were taken as the professor explains why he teaches his class in Go. He also mentioned he'd be able to teach it with Python or Java. He used C++ years ago.

**The beginning of this lecture was a great summary of:**

-  key benefits of Golang
-  what threads are and why they're great
-  how Go, threads and async tie together

**Go is Good for Distributed Systems**

Go is concurrency-friendly. With concurrent threads, you can effectively split a task such as making web requests to a server into many threads, completing them simultaneously.

**Golang's Convenient Features and Benefits**

-  convenient `Remote Procedure Call library <https://golang.org/pkg/net/rpc/>`__ (`RPC <https://en.wikipedia.org/wiki/Remote_procedure_call>`__) C++ lacks anything comparable?
-  "Go is type-safe and memory-safe, unlike C++"
-  `garbage collection <https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)>`__
-  "the language is simple, unlike C++"
-  "good support for threads, `locking <https://en.wikipedia.org/wiki/Lock_(computer_science)>`__ and synchronization between threads"
-  in Go, "`goroutines <https://golang.org/doc/effective_go.html#goroutines>`__" are threads
-  professor's recommended reading to learn Go: `Effective Go <https://golang.org/doc/effective_go.html>`__

**Why use threads?**

-  I/O Concurrency
-  Multi-core `Parallelism <https://en.wikipedia.org/wiki/Parallel_computing#:~:text=Parallel%20computers%20can%20be%20roughly,work%20on%20the%20same%20task.>`__
-  Convenience, e.g. "create 10 threads that sleep for a second and then do a little bit of work"

..

   "Threads are the main tool we're using to manage concurrency in programs."

   -Prof. Robert Morris

**Contrast With**\ `Event-driven Programming <https://en.wikipedia.org/wiki/Event-driven_programming#:~:text=In%20computer%20programming%2C%20event%2Ddriven,from%20other%20programs%20or%20threads.>`__\ **("Asynchronomous")**

A single thread, single loop that waits for an event.

**Combining Threads and Event Driven Programming**

   "Create one thread for each procedure call."... "On each of the threads run a stripped down event driven loop. Sort of one event loop per core. That results in parallelism and I/O concurrency."

   -Prof. Robert Morris

**Postface: Concurrent Python Context**

I've rarely if ever used multiple threads in Python. Simply running a single threaded script seems sufficient for most of my tasks. Maybe I could speed up API requests by splitting into threads when making a few hundred thousand requests? Apparently I'm missing out on concurrent threading efficiency gains.

I once experimented with the `multiprocessing <https://docs.python.org/3.8/library/multiprocessing.html>`__ module's `Process class <https://docs.python.org/3.8/library/multiprocessing.html#the-process-class>`__, which worked on Linux but not Windows for me. I ended up taking an simpler, single thread approach instead. I've also heard of using multiprocessing `pool <https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool>`__ objects. There's also the `asyncio <https://docs.python.org/3/library/asyncio.html>`__ library `concurrent.futures <https://docs.python.org/3/library/concurrent.futures.html>`__ modules to consider. The `ProcessPoolExecutor <https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor-example>`__ looks promising.

Python also has the `queue module. <https://docs.python.org/3/library/queue.html>`__ I haven't used it yet but at one point I watched a talk where `Raymond Hettinger <https://www.youtube.com/watch?v=_GP9OpZPUYc>`__ recommended queue as a good option if you want concurrency in Python.

It seems there are many options available in Python but it's not clear which tools should be deployed and when. And your chosen concurrency strategy may add extra complexity. Handle with care. Or consider learning Go if you want to use threads to scale your distributed system.

**Update: Python Concurrency Success**

I recently deployed the `ThreadPoolExecutor <https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor>`__ from the concurrent.futures module to efficiently move thousands of files to a new folder. So Python does have fairly accessible alternatives to concurrency. I guess I'll need to try Go sometime to compare!

.. code:: wp-block-syntaxhighlighter-code

   from concurrent.futures import ThreadPoolExecutor
   import numpy as np
   import shutil
   import os

   """
   Move files concurrently from the 
   current working directory to a new folder.

   This script is adapted from the Python 
   ThreadPoolExecutor documentation:
   https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.shutdown

   disclaimer: I am new to concurrency. Not 100% sure 
   if I am using the ThreadPoolExecutor correctly 
   but it seems to work, by moving my files concurrently and fast.
   """
   csvs = [f for f in os.listdir(os.getcwd()) if '.csv' in f]
   split_num = len(csvs) / 4 + 1
   file_batches = np.array_split(csvs, split_num)

   def main():
       with ThreadPoolExecutor(max_workers=4) as e:
           for i, files in enumerate(file_batches):
               csv_A, csv_B, csv_C, csv_D = files
               e.submit(shutil.move, csv_A, dst_folder)
               e.submit(shutil.move, csv_B, dst_folder)
               e.submit(shutil.move, csv_C, dst_folder)
               e.submit(shutil.move, csv_D, dst_folder)
                           
   if __name__ == '__main__':
       main()

**Additional Reading**

`New Case Studies About Google's Use of Go <https://opensource.googleblog.com/2020/08/new-case-studies-about-googles-use-of-go.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+GoogleOpenSourceBlog+%28Google+Open+Source+Blog%29>`__

`go.dev <https://go.dev/>`__
