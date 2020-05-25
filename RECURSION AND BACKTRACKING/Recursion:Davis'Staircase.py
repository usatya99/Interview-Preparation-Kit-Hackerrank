#BACKTRACKING AND RECURSION
#RECURSION:DAVIS'STAIRCASE

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n,p):
    l=[0]*(50)
    l[0],l[1],l[2],l[3]=0,1,2,4
    for i in range(4,n+1):
        l[i]=l[i-3]%p+l[i-2]%p+l[i-1]%p
    return l[n]%p
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())
        p=10000000007
        res = stepPerms(n,p)%10000000007

        fptr.write(str(res) + '\n')

    fptr.close()
