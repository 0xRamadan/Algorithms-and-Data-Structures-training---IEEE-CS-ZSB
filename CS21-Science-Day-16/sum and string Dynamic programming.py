# name: Mahmoud Abdallah Hassan
# mail: mahmoud.abdallah@ieee-zsb.org
# link: https://www.hackerrank.com/challenges/sam-and-substrings/problem
# time complexity: O(n)

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    Mod = (10**9)+7
    t = 1
    total = 0
    for i, digit in enumerate(reversed(n)):
        total += t * digit * (len(n)-i) % Mod
        t = (10 * t +1) % Mod  
    return total % Mod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = list(map(int, list(sys.stdin.readline().strip())))

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
