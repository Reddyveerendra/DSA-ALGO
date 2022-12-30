from os import *
from sys import *
from collections import *
from math import *

def maxSubSumKConcat(arr, n, k):
    arr=arr*k
    maxsum=min(arr)
    temp=0
    for i in range(n*k):
        temp=max(arr[i],temp+arr[i])
        maxsum=max(maxsum,temp)
        if(temp<0):
            temp=0
    return maxsum