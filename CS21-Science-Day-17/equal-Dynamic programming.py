# name: Mahmoud Abdallah Hassan
# mail: mahmoud.abdallah@ieee-zsb.org
# link: https://www.hackerrank.com/challenges/equal/problem
# time complexity: O(n)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equal function below.
def equal(arr):
    listOfMin_Operation = [0]*5
    t = min(arr)
    for m in range(5):
        # reset min number to 0
        NumberOfOperation = 0 
        for i in range(len(arr)):
            v = arr[i] - t + m
            add5 = v//5
            add2  = v%5//2
            add1  = v%5%2
            NumberOfOperation += add5 + add2 + add1
        # store this number
        listOfMin_Operation[m] = NumberOfOperation 
    return min(listOfMin_Operation)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()