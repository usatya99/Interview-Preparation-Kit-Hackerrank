#GREEDY ALGORITHMS
#LUCK BALANCE

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck,result=[],0
    for i in contests:
        if i[1]==1:
            luck.append(i[0])
        else:
            result+=i[0]
    luck.sort(reverse=True)
    print(luck,result)

    return (result+sum(luck[:k]))-sum(luck[k:])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
