#RECURSION AND BACKTRACKING
#RECURSIVE DIGIT SUM

#!/bin/python3

import math
import os
import random
import re
import sys

def sum1(n):
    if len(n)==1:
        return n
    else:
        c=str(sum([int(i) for i in n]))
        return sum1(c)
# Complete the superDigit function below.
def superDigit(n, k):
    bm=sum1(n)*k
    result=sum1(bm)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
