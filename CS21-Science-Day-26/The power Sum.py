#
# CS21-Science-Day-26
# Name: Mahmoud Abdallah Hassan
# GitHub link: https://github.com/RaymondReddigton
# problem link: https://www.hackerrank.com/challenges/the-power-sum/problem
#
#

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(total, power, num):
    value = (total - pow(num, power))
    if value < 0:
        return 0
    elif value == 0:
        return 1
    else:
        return powerSum(value, power, num+1)+powerSum(total, power, num+1)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    total = int(input())

    power = int(input())

    result = powerSum(total, power, 1)

    fptr.write(str(result) + '\n')

    fptr.close()