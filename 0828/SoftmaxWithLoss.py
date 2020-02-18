#!/usr/bin/env python
# coding: utf-8

# In[2]:


class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None
    
    def forward(self,x,t):
        # x 是輸入
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self,y,self.t)
        return self.loss
    
    def backward(self,dout):
        batch_size = self.t.shape[0]
        dx = (self.y-self.t) / batch_size
        return dx
    
    
    

