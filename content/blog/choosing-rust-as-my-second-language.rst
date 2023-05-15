Reasons to Explore Rust and A Brief Intro
#########################################
:date: 2019-08-19 02:17
:author: pythonmarketer
:category: coding, programming, Rust, software, WebAssembly
:slug: choosing-rust-as-my-second-language
:status: published

Four years ago, I began studying Python as my first programming language. I have enjoyed it so much. I now enjoy going to work and writing Python scripts for up to 60% of a typical work day. I love the language. I've also dabbled in JavaScript, CSS and HTML, but have only applied those to make simple, minimum viable websites. So why learn another language, Rust?

#. **Learning multiple languages enhances one's understanding of computing.** All languages tackle the same problems in different ways. Some leverage trade-offs enabling them to better solve specific computing problems than others. Seeing different approaches to the same challenges increases your understanding of the concepts.
#. **Rust is beloved by its developers.** It scored highly on `Stack Overflow's 2019 developer survey <https://insights.stackoverflow.com/survey/2019>`__. The most loved language was Rust, with 83.5% of developers saying they loved it. Python was tied for 2nd at 73.1% with TypeScript.
#. **Rust is an LLVM language, Python is not.** Per `Wikipedia <https://en.wikipedia.org/wiki/LLVM>`__, "The LLVM `compiler <https://en.wikipedia.org/wiki/Compiler>`__ infrastructure project is a set of compiler and `toolchain <https://en.wikipedia.org/wiki/Toolchain>`__ technologies, which can be used to develop a `front end <https://en.wikipedia.org/wiki/Compiler#Front_end>`__ for any `programming language <https://en.wikipedia.org/wiki/Programming_language>`__ and a `back end <https://en.wikipedia.org/wiki/Compiler#Back_end>`__ for any `instruction set architecture <https://en.wikipedia.org/wiki/Instruction_set_architecture>`__." It seems Rust opens up modularity to mesh with a bunch of other LLVM languages. Side note: `LLVM started <https://en.wikipedia.org/wiki/LLVM>`__ at my alma mater, the University of Illinois at Urbana-Champaign 😃 ILL 🔶🔷

..

   LLVM was originally developed as a research infrastructure to investigate `dynamic compilation <https://en.wikipedia.org/wiki/Dynamic_compilation>`__ techniques for static and `dynamic <https://en.wikipedia.org/wiki/Dynamic_programming_language>`__ `programming languages <https://en.wikipedia.org/wiki/Programming_language>`__. -`Wikipedia <https://en.wikipedia.org/wiki/LLVM>`__

4. **Rust plays well with WebAssembly.** AKA `Wasm <https://webassembly.org/>`__, a new standard introduced in 2015 that allows compilation of high performance browser or Desktop applications. I am still grappling with why Wasm is getting so much hype, but it seems to be a big deal. Rust opens doors to Wasm compatibility. Python is Wasm capable as well but I am getting the impression there is something in Rust's design that makes it useful for compiling to Wasm.
5. **It is a modern language, which surfaced in 2010, that is still coming of age.** This is both good and bad. But the good here is modern language design. Its creator saw the shortcomings of countless languages that have come before it. An enthusiastic community has already made Rust a good programming language option in a short time.

**Getting Started with Rust**

The `Getting Started <https://www.rust-lang.org/learn/get-started>`__ page contains a simple curl command for downloading and installing Rust via "Rustup", an installer and version management tool. This will install Cargo, Rust's package manager. (Think pip for Pythonistas.) I used my Linux environment on my Chromebook, but there's a `Windows executable <https://doc.rust-lang.org/cargo/getting-started/installation.html>`__ available as well.

.. container:: row

   .. code:: instructions

      curl https://sh.rustup.rs -sSf | sh

   .. container::

.. image:: http://pythonmarketer.files.wordpress.com/2019/08/b2024-rust_startup-e1566179301570.png
   :alt: rust_startup.png
   :class: alignnone size-full wp-image-1917
   :width: 814px
   :height: 857px

[gallery type="rectangular" size="full" columns="1" link="file" ids="1918"]

`The Cargo Book <https://doc.rust-lang.org/cargo/index.html>`__ provides documentation for the package manager. I like the "`First Steps with Cargo <https://doc.rust-lang.org/cargo/getting-started/first-steps.html>`__" section because it gets you immediately into creating and running a "build" by entering a few short commands in the terminal.

| **Create a New Build**
| ``cargo new hello_world``

````\ |Rust_Hello_World|

**cd Into Your hello_world Program**

Note the creation of a .toml manifest, and simple Rust program that prints "Hello, world!".

| **Compile and Run Your Program**
| ``cargo run``

.. image:: http://pythonmarketer.files.wordpress.com/2019/08/1d7ac-rust_cargo_run-e1566178950427.png
   :alt: Rust_cargo_run
   :class: alignnone size-full wp-image-1916
   :width: 781px
   :height: 84px

Now, on to learning the syntax, which is often compared to languages like C and C++. First stop for me will be "the book",\ `The Rust Programming Language <https://doc.rust-lang.org/book/>`__\ . Cheers :)

**See also:** `Rust Cheat Sheet <https://cheats.rs/>`__

.. |Rust_Hello_World| image:: http://pythonmarketer.files.wordpress.com/2019/08/15b99-rust_hello_world-e1566179455440.png
   :class: alignnone size-full wp-image-1919
   :width: 788px
   :height: 50px
