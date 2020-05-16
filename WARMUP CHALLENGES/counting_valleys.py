#WARM-UP CHALLENGES
#COUNTING VALLEYS
#!/bin/python3

import math

import os

import random

import re

import sys

# Complete the countingValleys function below.

def countingValleys(n, s):

    c=0

    v=0

    for i in s:

        if i=='U':

            c+=1

        if i=="D":

            c-=1

        if c==0 and i=='U':

            v+=1

    return v

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

