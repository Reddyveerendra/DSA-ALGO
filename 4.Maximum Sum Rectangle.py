from os import *
from sys import *
from collections import *
from math import *
import sys
def maxSumRectangle(arr, n, m):
    s=-sys.maxsize-1
    for i in range(n):
        a=[0]
        a=a*m
        for j in range(i,n):
            for k in range(m):
                a[k]+=arr[j][k]
            c=0
            for l in range(m):
                c=c+a[l]
                s=max(s,c)
                if(c<0):
                    c=0
    return s