=====================
BBS Code Highlighter
=====================

Inspired by `this post`_. This utility is a simple custom formatter that can be
used with Pygments_.


------
Howto
------

To use the formatter, simply run the Pygments script like this:

::

    pygmentize -f bbs -l <source language> <file to format>

Or you can write your own script an take advantage with Pygments's API. The
formatter class is at ``bbshighlighter.formatters.BBSFormatter``

A simple Django project is attached in directory ``haas`` (stands for
"Highlighter as a Service," of course) to serve the formatter as a web app. You
can see it in action at http://bbshighlighter.uranusjr.com/.


--------
License
--------

This project is published under the BSD 3-cluse license. See the content of
file ``LICENSE``.


.. _this post: http://www.ptt.cc/bbs/C_and_CPP/M.1393408128.A.4E6.html
.. _Pygments: http://pygments.org
