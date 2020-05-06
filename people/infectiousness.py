# -*- coding: utf-8 -*-
"""
Created on Wed May  6 22:28:22 2020

@author: sgnodde
"""


import numpy as np


def linear(age):
    return age/200+0.5


def logarit(age):
    return np.log(age+1)/np.log(101)