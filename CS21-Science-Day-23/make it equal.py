#
# CS21-Science-Day-23
# Name: Mahmoud Abdallah Hassan
# GitHub link: https://github.com/RaymondReddigton
# problem link: https://codeforces.com/contest/1065/problem/C
# Time Complexity: O(n^2)
#
#

if __name__ == "__main__":
    numOfTowers, numOfOperation = map(int, input().split())
    towerheights = list(map(int, input().split()))
    towerheights.sort(reverse=True)

    # print(towerheights)
    # [4, 3, 2, 2, 1]

    counter = 0 
    lowerheight = towerheights[-1]
    higherheight = towerheights[0]
    nextheightindex = 1
    minNumOfgoodSlices = 0
    while higherheight != lowerheight:
        while higherheight == towerheights[nextheightindex]:
            nextheightindex += 1
        
        if counter + nextheightindex > numOfOperation:
            minNumOfgoodSlices += 1
            counter = nextheightindex
        else:
            counter += nextheightindex
        higherheight -= 1

    if counter > 0:
        minNumOfgoodSlices += 1
    print(minNumOfgoodSlices)