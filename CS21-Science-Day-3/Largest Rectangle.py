#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
# def largestRectangle(h):
#     h.sort()
#     max_rec_list = []
#     for i in range(len(h)):
#         max_rec_list.append(h[i]*(len(h)-i))
#     max_rec = max(max_rec_list)
#     return max_rec

# def largestRectangle(h):
#     height = pos = 0
#     hstack = []
#     pstack = []
#     maxArea = 0
#     tempPos = 0 
#     def popElement():
#         tempHeight = hstack.pop()
#         tempPos = pstack.pop()
#         tempArea = tempHeight * (pos - tempPos)
#         maxArea = max(tempArea, maxArea)
        

#     for pos in range(len(h)):
#         height = h[pos]
#         if not hstack or height > hstack[len(hstack)-1]:
#             hstack.append(height)
#             pstack.append(pos)
#         elif(height < hstack[len(hstack)-1]):
#             while hstack and (height < hstack[len(hstack)-1]):
#                 tempHeight = hstack.pop()
#                 tempPos = pstack.pop()
#                 tempArea = tempHeight * (pos - tempPos)
#                 maxArea = max(tempArea, maxArea)
        
#             if not hstack:
#                 hstack.append(height)
#                 pstack.append(tempPos)

#     while hstack:
#         tempHeight = hstack.pop()
#         tempPos = pstack.pop()
#         tempArea = tempHeight * (pos - tempPos)
#         maxArea = max(tempArea, maxArea)
        
#     return maxArea


def largestRectangle(h):
    stack = []
    area = i = 0
    h.append(0)
    while i < len(h):
        if not stack or h[i] > h[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            area = max(area, h[top] * (i - stack[-1] - 1 if stack else i))
    return area


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
