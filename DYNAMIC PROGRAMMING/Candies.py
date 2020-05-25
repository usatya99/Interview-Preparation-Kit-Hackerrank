#DYNAMIC PROGRAMMING
#CANDIES


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, l):
    left=[0]*n
    left[0]=1
    right=[0]*n
    right[n-1]=1
    for i in range(1,n):
        if l[i]<=l[i-1]:
            left[i]=1
        else:
            left[i]=left[i-1]+1
    for i in range(n-2,-1,-1):
        if l[i]<=l[i+1]:
            right[i]=1
        else:
            right[i]=right[i+1]+1
    #print(left,right)
    sum1=0
    for i,j in zip(left,right):
        sum1+=max(i,j)        
    return sum1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
