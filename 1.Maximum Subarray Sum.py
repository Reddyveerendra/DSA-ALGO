from os import *
from sys import *
from collections import *
from math import *
import sys
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    maxsum=0
    count=0
    for i in range(n):
        count=count+arr[i]
        maxsum=max(maxsum,count)
        if(count<0):
            count=0
    return maxsum

#taking inpit using fast I/O
def takeInput() :
    
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))