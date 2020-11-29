def createSnakeTower(n, snacks):
    
    visitedSnacks = [None] * n
 
    for snack in snacks:
        visitedSnacks[int(snack)-1] = snack
 
        while visitedSnacks[n-1] and n != 0:
            print("{0}".format(n), end=" ")
            n -= 1
        print("")
 
 
if __name__ == "__main__":
    n = int(input().strip())
    s = input().split()
 
    createSnakeTower(n, s)