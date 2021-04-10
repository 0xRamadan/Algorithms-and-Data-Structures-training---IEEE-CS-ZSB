#
# CS21-Science-Day-24
# Name: Mahmoud Abdallah Hassan
# GitHub link: https://github.com/RaymondReddigton
# problem link: https://codeforces.com/contest/445/problem/C
# Time Complexity: O(n)
#
#


nodes , edges = map(int, input().split())
  
nodesValues= list(map(int, input().split()))
 
answer = 0
 
for i in range(edges):
  
    a, b, c = map(int,input().split())
    
    answer  = max(answer , (nodesValues[a-1] + nodesValues[b-1])/c)
    
print(answer)