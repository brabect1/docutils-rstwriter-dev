Docutils `rst` Writer
=====================

The `docutils-rstwiter` converts reStructuredText to reStructuredText. The sole
purpose of this endeavour, as odd as it may seem, is to convert a `rst` document
distributed over multiple files (and bound through `include` statements) into
a single `rst` document that may be further processed.

The rationale is that some other `rst` processing tools such as
[pandoc](https://pandoc.org/) do not handle well deep, multi-level `include`s
in `rst`.

There has also been an earlier [rst2rst](https://github.com/benoitbryon/rst2rst)
writer, but it is quite dated and far from complete.

