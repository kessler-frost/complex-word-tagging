# Complex Word Identification
This project uses machine learning to detect complex words and give hyperlinks to their meanings in a .docx file, from a given .txt file. This is a fork from a private ongoing project of ours. Currently this project is (kind of) usable by the general public (read: people who know how to run python scripts).

# Prerequisites
I recommend you should use **Anaconda Distribution** to avoid any errors while execution. Also this script is written in Python 3 so make sure you are using the correct version of python before proceeding.


There are certain packages which are required to execute this including,
1. nltk
2. docx
3. numpy


Test that whether you already have these by simply running a python shell in your terminal/cmd and executing,

**import <_package_name_>**

# Instructions
First you will need to clone this repository and open a shell inside this directory.
*The following commands are tested on macOS but should work in other OSes without any trouble.*

Copy the text file, from which you want to extract complex words, to this directory and execute,

```
  python hyperlink_complex.py **INSERT_FILENAME_WITH_EXTENSION**
```

This will create a .docx file of name :- **\<filename\>\_tcw.docx** (tcw -> tagged complex words)


This file contains the given text alongwith the tagged complex words with hyperlinks to the **Merriam-Webster** website containing their meanings.
