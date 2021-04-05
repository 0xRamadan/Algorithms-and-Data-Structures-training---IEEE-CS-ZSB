if __name__=='__main__':
    typesOfSoliders, players , armies = map(int,input().split())
    soliders = []
    friends = 0

    for i in range(players+1):
        soliders.append(int(input()))

    for i in range(players):

        commonSoliders = bin(soliders[i]^soliders[-1]).count('1')
        if commonSoliders <= armies:
            friends += 1

    print(friends)