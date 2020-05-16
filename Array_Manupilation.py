#ARRAYS
#ARRAY MANIPULATION
#!/bin/python3  

import math

import os

import random

import re

import sys

# Complete the arrayManipulation function below.

def arrayManipulation(n, queries):

    l=[0]*(n+1)

    for i in (queries):

        a,b,s=i[0],i[1],i[2]

        l[a-1]+=s

        if(b<=len(l)):

            l[b]-=s

    x,res=0,0

    for j in l:

        x+=j

        if(res<x):

            res=x

    return res

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):

        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

