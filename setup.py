#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
     
setup(name="PackageName",
    ext_modules=[
        Extension("interval_tree_wrap", ["interval_tree_wrap.cpp"],
        libraries = ["boost_python"])
    ])