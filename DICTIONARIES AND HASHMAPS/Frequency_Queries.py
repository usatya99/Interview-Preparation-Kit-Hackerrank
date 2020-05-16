#DICTIONARIES AND HASHMAPS
#FREQUENCY QUERIES
 #!/bin/python3

import math

import os

import random

import re

import sys

from collections import Counter,defaultdict

# Complete the freqQuery function below.

def freqQuery(queries):

    ans=[]

    d=defaultdict(int)

    f=defaultdict(set)

    for c,v in queries:

        if c==1:

            d[v]+=1

        elif c==2:

            if d[v]>0:

                d[v]-=1

        else:

            if f[v] and v in d.values():

                ans.append(1)

            else:

                ans.append(0)

        f[d[v]].add(v)

    return ans

            

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):

        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))

    fptr.write('\n')

    fptr.close()

