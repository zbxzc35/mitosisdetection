# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 20:52:12 2016

@author: btek
"""


def listDiff(a, b):
    return lambda la, lb: [x for x in la if x not in lb]
