#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ReLU function

class Relu:
    # 初始化
    def __init(self):
        self.mask = None
    # 函數需求，要轉為布林值，判斷 x 是否小於 0，但 false 屬性不是我們要的
    def forward(self):
        self.mask=(x<=0)
        out =x.copy()
        out[self.mask]=0
        return out
    def backward(self,dout):
        dout[self.mask]=0
        dx = dout
        return dx
    

