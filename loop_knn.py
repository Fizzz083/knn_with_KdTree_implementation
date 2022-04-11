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

cnt = [0]*(k+1)
ans = []
kk = k
for i in range(len(a)):
    if(k>0):
        k = k-1
        ans.append((X[a[i][1]],a[i][0]))
        #cnt[X[a[i][1]][2]] = cnt[X[a[i][1]][2]]+1
    else:
        break
    #print(str(a[i][0])+" "+str(X[a[i][1]]))

#ans.sort(key = lambda pair : pair[0])

for i in ans:
    cnt[i[0][2]]  = cnt[i[0][2]] +1
    print(i[1])


arr = []
print(kk)
for i in range(0, kk+1):
    #print(cnt[i])
    if(cnt[i]!=0):
        #print("j")
        arr.append((cnt[i],i))

arr.sort()
#print(cnt)
#print(len(arr))
#print(arr)
print("Best Class : " + str(arr[-1][1]) + " cnt: " + str(arr[-1][0]))