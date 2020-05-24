#SEARCH
#TRIPLE SUM

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a=list(sorted(set(a)))
    b=list(sorted(set(b)))
    c=list(sorted(set(c)))
    a1=0
    b1=0
    c1=0
    count=0
    while(b1<len(b)):
        while(a1<len(a) and a[a1]<=b[b1]):
            a1+=1
        while(c1<len(c) and c[c1]<=b[b1]):
            c1+=1
        count+=a1*c1
        b1+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
