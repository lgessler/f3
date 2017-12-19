f3 (word Frequencies From Files)
================================

This tool takes in a text file and outputs the frequencies of the words in that text file as a TSV. Currently, windows-1252, ISO-8859-1, ascii, UTF-8, UTF-16, and UTF-32 encodings are supported. Output is always in UTF-8.

## Setup

You'll need to do some setup to get this to work. At the root of this repository, execute the following shell commands:

```
pip3 install -r requirements.txt
```

## Examples

Example invocations without installing: 

```
# TSV using regular expression tokenizer
python3 f3/__main__.py sourcefile.txt outfile.tsv

# same as above, but ignore case
python3 f3/__main__.py --ignore-case sourcefile.txt outfile.tsv

# attempt to filter out a "junk language": use --filter-junk and also set values
# for flags --target-lang and --junk-lang. This is for a corpus in Swahili
# that contains junk data in English.
python3 f3/__main__.py --filter-junk sourcefile.txt outfile.tsv --target-lang sw --junk-lang en
```

## Install

To install `f3` as a CLI tool, type

```
python3 setup.py develop
```

This should have installed `f3` to `/usr/local/bin`. You should now be able to use it from the command line:

```
f3 -h
```
