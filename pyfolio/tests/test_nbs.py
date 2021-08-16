#!/usr/bin/env python
"""
simple example script for running notebooks and reporting exceptions.
Usage: `checkipnb.py foo.ipynb [bar.ipynb [...]]`
Each cell is submitted to the kernel, and checked for errors.
"""

import os
import glob
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
# from pyfolio.ipycompat import read as read_notebook


def test_nbs():
    path = os.path.join('..', 'examples', '*.ipynb')
    for ipynb in glob.glob(path):
        with open(ipynb) as f:
            # nb = read_notebook(f, 'json')
            nb = nbformat.read(f, as_version=4)
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            ep.preprocess(nb)
