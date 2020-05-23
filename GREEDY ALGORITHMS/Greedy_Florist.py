#GREEDY ALGORITHMS
#GREEDY FLORIST

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort()
    if k>=len(c):
        return sum(c)
    else:
        result=0
        previous=0
        temp=0
        for i in range(len(c)-1,-1,-1):
            if temp==k:
                temp=0
                previous+=1

            result+=(previous+1)*c[i]
            temp+=1
        return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
