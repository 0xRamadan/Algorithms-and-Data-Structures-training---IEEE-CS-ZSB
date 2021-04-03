#
# CS21-Science-Day-20
# Name: Mahmoud Abdallah Hassan
# GitHub link: https://github.com/RaymondReddigton
# problem link: https://codeforces.com/contest/810/problem/B
# Time Complexity: n log(n)
#
#

numOfDays, sellOffDays = map(int, input().split())
totalProductsSold = 0
l = []
for i in range(numOfDays):
    numOfProduct, numOfClients = map(int, input().split())
    totalProductsSold += min(numOfProduct, numOfClients)
    l.append(min(2*numOfProduct, numOfClients)-min(numOfProduct,numOfClients))
l.sort()
print(totalProductsSold+sum(l[numOfDays-sellOffDays: ]))