from os import *
from sys import *
from collections import *
from math import *

def flipBits(arr, n): 
    # Write your code here
    c=0
    s=0
    t=0
    for i in range(n):
        if(arr[i]==0):
            c=c+1
        else:
            c=c-1
            t=t+1
        s=max(s,c)
        if(c<0):
            c=0
    return s+t