#STRING MANIPULATION
#ALTERNATING CHARACTERS

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    #CASE 1
    if s.startswith('A'):
        a='A'
        b='B'
        c=0
        for i in range(len(s)-1):
            if s[i]==a and s[i+1]==b:
                a,b=b,a
            else:
                c+=1
        return c
    #CASE 2
    else:
        a='B'
        b='A'
        c=0
        for i in range(len(s)-1):
            if s[i]==a and s[i+1]==b:
                a,b=b,a
            else:
                c+=1
        return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
