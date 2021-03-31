# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:07:25 2021

@author: mohsen
"""


import numpy as np

def new_func():
    
    return

def say_hello(name,last_name,language):
    if language == 'English':
        print('Hello!'+ 'Mr./Ms.'+ last_name)
    elif language == 'Italian':
        print('Buogiorno!'+ 'Signore/ Signora'+ last_name)
    return


say_hello('Marzieh','Bathaee','Italian')
say_hello('Abbas', 'Shojakani','English')