#SEARCH
#HASH TABLES : ICE CREAM PARLOR

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    z={}
    for pos,cost1 in enumerate(cost):
        s2=money-cost1
        if s2 in z:
            print(z[s2],pos +1)
            break
        else:
            z[cost1]=pos+1 
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
