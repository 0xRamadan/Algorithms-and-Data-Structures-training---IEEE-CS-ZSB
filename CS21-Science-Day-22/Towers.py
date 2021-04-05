#
# CS21-Science-Day-22
# Name: Mahmoud Abdallah Hassan
# GitHub link: https://github.com/RaymondReddigton
# problem link: https://codeforces.com/contest/479/problem/B
# Time Complexity: O(n)
#
#


numOfTowers, numOfOperations = map(int, input().split())
heights = list(map(int, input().split()))
l = []
for i in range(numOfOperations):
    max_index = heights.index(max(heights))
    min_index = heights.index(min(heights))

    if min_index != max_index:
        heights[max_index] -= 1
        heights[min_index] += 1
        l.append([max_index+1, min_index+1])

print(max(heights)-min(heights), len(l))
for j in l:
    print(' '.join(map(str, j)))
