#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

class Sigmoid:
    def __init__(self):
        self.out = None
    def forward(self,x):
        out - 1/(1 + np.exp(-x))
    def backward(self,dout):
        dx = dout*(1-self.out)*self.out
        return dx
    

