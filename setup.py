#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Adam Buran"
__version__ = ""
__contact__ = "aburan28@gmail.com"







#!/usr/bin/env python
from distutils.core import setup, Extension
from Cython.Distutils import build_ext
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy



ext = Extension("", [".pyx"],
    include_dirs = [numpy.get_include()],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp']
    )







setup(ext_modules=[ext],
      cmdclass = {'build_ext': build_ext})
