# Problem link: https://www.hackerrank.com/challenges/utopian-tree/problem
# problem name: Utopain Tree
# CS21-Science-Day-28
# github: @RaymondReddigton

import math
import os
import random
import re
import sys


def utopianTree(numOfCycles):
    # Write your code here
    height = 0
    for i in range(numOfCycles+1):
        height = height+1 if i%2==0 else height*2
    return height
 

if __name__ == '__main__':
    
    numberOftestCases = int(input().strip())

    for testCase_itr in range(numberOftestCases):
        numOfCycles = int(input().strip())

        result = utopianTree(numOfCycles)

        print(result)
