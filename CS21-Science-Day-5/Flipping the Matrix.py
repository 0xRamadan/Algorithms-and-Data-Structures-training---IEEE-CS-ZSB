#
#       CS21-Science-Day-05
#       name: Mahmoud Abdallah 
#       task: Flipping the Matrix
#       link: https://www.hackerrank.com/challenges/flipping-the-matrix/problem?isFullScreen=false
#


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingMatrix function below.
def flippingMatrix(matrix):
    n = len(matrix[0])
    for i in range(n):
        for j in range(n):
            print(sum([max(matrix[i][j]), matrix[i][2*n - 1 - j], matrix[2*n - 1 - i][j], matrix[2*n -1 -i][2*n -1 -j]]))




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        matrix = []

        for _ in range(2*n):
            # row by row; each row is a list
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        print(str(result))

        fptr.write(str(result) + '\n')

    fptr.close()

