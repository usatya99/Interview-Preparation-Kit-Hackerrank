#MISCELLANEOUS
#FLIPPING BITS



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    a=bin(n)[2:]
    zero=32-len(a)
    res=('0'*zero)+a
    result=''
    for i in res:
        if i=='0':
            result+='1'
        else:
            result+='0'
    return(int(result,2))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

