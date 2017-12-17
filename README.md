f3 (word Frequencies From Files)
================================

This tool takes in a text file and outputs the frequencies of the words in that text file as a TSV. Currently, windows-1252, ISO-8859-1, ascii, UTF-8, UTF-16, and UTF-32 encodings are supported. Output is always in UTF-8.

## Install

Package requirements are handled using pip. To install them do

```
pip3 install -r requirements.txt
```

Then, to install `f3` as a CLI tool, type

```
python3 setup.py develop
```

This should have installed `f3` to `/usr/local/bin`. You should now be able to use it from the command line:

```
f3 [-ih] source dest
```
