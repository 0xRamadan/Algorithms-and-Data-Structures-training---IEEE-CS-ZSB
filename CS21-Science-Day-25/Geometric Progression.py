#
# CS21-Science-Day-25
# Name: Mahmoud Abdallah Hassan
# GitHub link: https://github.com/RaymondReddigton
# problem link: https://codeforces.com/contest/567/problem/C
# Time Complexity: O(nlog(n))
#
#

import collections
numOfSequence, favNum = map(int, input().split())
dic=[collections.defaultdict(int)for _ in"123"]

for elementInSeq in map(int, input().split()):
    dic[2][favNum*elementInSeq]+=dic[1][elementInSeq]
    dic[1][favNum*elementInSeq]+=dic[0][elementInSeq]
    dic[0][favNum*elementInSeq]+=1

# print(dic)
print(sum(dic[2].values()))