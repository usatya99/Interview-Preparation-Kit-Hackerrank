#SEARCH
#PAIRS

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr.sort()
    c=0
    i=0
    j=1
    size=len(arr)
    while(i<size and j<size):
        if arr[j]-arr[i]==k:
            c+=1
            j+=1
        elif arr[j]-arr[i]<k:
            j+=1
        else:
            i+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
