# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 04:58:36 2022

@author: USER
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



X = []
y = []

n = int(input())
k = int(input())
for i in range(n):
    x1, y1,c = map(int, input().split())
    X.append((x1, y1,c))


cx, cy = map(int, input().split())

a = []

for i in range(n):
    di = ((cx-X[i][0])*(cx - X[i][0])) + ((cy - X[i][1])*(cy - X[i][1]))
    a.append((di, i))

a.sort(key=lambda pair: pair[0])
ans = []
for i in range(len(a)):
    if(k>0):
        k = k-1
        ans.append((X[a[i][1]],a[i][0]))
    #print(str(a[i][0])+" "+str(X[a[i][1]]))

ans.sort(key = lambda pair : pair[0])

for i in ans:
    print(i)
