# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
tlist = [1,2,3,4,5,6,7,8,9,10]
tlist[-2]



size = 4




import numpy as np

a = np.zeros(shape=(10001, 101, 1))
b = a.reshape(101,10001)
c = b.reshape(1, b.shape[0], b.shape[1])
b.shape[-1]

weights_0_1 = np.random.randn(10,5)
indices = [4,9]

layer_1 = np.zeros(5)

for index in indices:
    layer_1 += (1 * weights_0_1[index])
    
layer_1