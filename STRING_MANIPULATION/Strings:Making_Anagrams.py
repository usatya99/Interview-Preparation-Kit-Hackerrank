#STRING MANIPULATION
#STRINGS:MAKING ANAGRAMS

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dict1={}
    dict2={}
    for i in a:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    for i in b:
        if i in dict2:
            dict2[i]+=1
        else:
            dict2[i]=1
    print(dict1,dict2)
    c=0
    for key,val in dict1.items():
        if key in dict2:
            c+=abs(dict1[key]-dict2[key])
            dict1[key]=0
            dict2[key]=0
    
    for i in dict1.values():
        if i>0:
            c+=i
    for i in dict2.values():
        if i>0:
            c+=i
    return(c)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
