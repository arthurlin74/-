#!/usr/bin/env python
# coding: utf-8

# In[7]:


# 梯度 gradient
# 對 x,y各自找斜率 (各自偏微分)，然後產生梯度
# 參考 https://zh.wikipedia.org/wiki/%E6%A2%AF%E5%BA%A6

import numpy as np
import os
import matplotlib.pylab as plt

# 3D繪圖模組
from mpl_toolkits.mplot3d import Axes3D

def function_2(x):
    return x[0]**2+x[1]**2

def numercial_gradient(f,x):
    h = -1e-4
    grad = np.zeros_like(x)
    for idx in range(x.size):
        
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxhl = f(x)
        x[idx] = tmp_val - h
        fxh2 = f(x)
        grad[idx] = (fxhl-fxh2) / (2*h)
        x[idx] = tmp_val
    
    return grad

# 這裡有浮點數運算問題，但原因不明
print("正確 :",numercial_gradient(function_2,np.array([3.0,4.0])))
print("錯誤 :",numercial_gradient(function_2,np.array([3,4])))

