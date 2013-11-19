#!/bin/bash

rst2html README.txt index.html
zip docs.zip index.html

python setup.py sdist --formats=gztar,zip upload
