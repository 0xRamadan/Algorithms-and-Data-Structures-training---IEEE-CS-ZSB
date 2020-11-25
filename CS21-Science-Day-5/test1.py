
n = int(input("enter n: "))

# list comprehension
matrix = [list(map(int, input().rstrip().split(" "))) for _ in range(2*n)]

print(matrix)

print("--------------")
s = []
for i in range(n):
    for j in range(n):
        s.append(max(matrix[i][j], matrix[i][2*n -1 -j], matrix[2*n - 1 - i][j], matrix[2*n -1 -i][2*n -1 -j]))

print(s)
print('sum of s: ', sum(s))



print("--------------")

print(sum([max(matrix[i][j], matrix[i][2*n - 1 - j], matrix[2*n - 1 - i][j], matrix[2*n -1 -i][2*n -1 -j]) for i in range(n) for j in range(n)]))

# flippingMatrix(m)


# 1 2 3 4
# 5 12 26 23
# 25 89 45 48
# 10 11 131 54
'''
example: 

 [[1,  2,   3,   4],               
  [5,  12, 26,  23],                 
  [25, 89, 45,  48],
  [10, 11, 131, 54]]


upper left quadrant sub matrix:
elements:
[54, 131, 48, 89]
how to det.:

i, j >> [0][0]
max([1, 4, 10, 54])   54
max([2, 3, 11, 131])  131
max([3, 2, 131, 11])  131
max([4, 1, 54, 10])  54


i, j >> [0][1]
max([5, 23, 25, 48])    48
max([12, 26, 89, 45])   89
max([26, 12, 54, 89])   89
max([23, 5, 48, 25])    48


 [[1,  2,   3,   4],               
  [5,  12, 26,  23],                 
  [25, 89, 45,  48],
  [10, 11, 131, 54]]

i, j >> [0][2]
max([25, 48, 5, 23])    48
max([89, 45, 12, 26])   89
max([])                 89
max([])                 48


i, j >> [0][3]
max([])                 54
max([])                 131
max([])                 131
max([])                 54

[max(--)] == [54, 131, 131, 54,
             48, 89, 89, 48,
             48, 89, 89, 48,
             54, 131, 131, 54]
'''


