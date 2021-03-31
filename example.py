# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:07:25 2021

@author: mohsen
"""


import numpy as np


def say_hello(name,last_name):
    print('Hello!'+ ' Mrs/Ms.'+ last_name)
    print('We hope you will be great ' + name)
    return


name = input('Enter your name: ').split()
say_hello(name[0],name[1])