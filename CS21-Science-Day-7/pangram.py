import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    s = set(s.lower()) 
  
    alpha = [ ch for ch in s if ord(ch) in range(ord('a'), ord('z')+1)] 
  
    return "pangram" if len(alpha) == 26 else "not pangram"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()