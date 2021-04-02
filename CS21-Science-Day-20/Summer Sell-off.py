if __name__ == "main":
    numOfDays, sellOffDays = list(map(int, input().split()))
    totalProductsSold = 0
    l = []
    for i in range(numOfDays):
        numOfProduct, numOfClients = map(int, input().split())
        totalProductsSold += min(numOfProduct, numOfClients)
        l.append(min(2*numOfProduct, numOfClients))
    l.sort()
    print(totalProductsSold + sum(l[numOfDays - sellOffDays:]))