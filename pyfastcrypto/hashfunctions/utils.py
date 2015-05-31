#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Adam Buran"
__version__ = ""
__contact__ = "aburan28@gmail.com"




#pythran export chunks(int, int)
def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

#pythran export rol(int, int)
def rol(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff
