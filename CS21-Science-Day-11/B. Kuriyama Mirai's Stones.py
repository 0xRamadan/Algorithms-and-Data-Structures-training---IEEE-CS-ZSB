# name: Mahmoud Abdallah Hassan
# mail: mahmoud.abdallah@ieee-zsb.org
# link: https://codeforces.com/problemset/problem/433/B
# time complexity: O(nlogn) 

if __name__ == "__main__":
    numberOfStones = int(input())

    costsOfStones = list(map(int, input().split()))
    
    costsOfStonesSorted = sorted(costsOfStones)  # O(nlogn)

    # creating prefix sum array
    for i in range(1, numberOfStones):  # O(n)
        # unsorted prefix
        costsOfStones[i] += costsOfStones[i-1]
        # sorted prefix
        costsOfStonesSorted[i] += costsOfStonesSorted[i-1]
        
    
    numberOfQuestions = int(input())
    for _ in range(numberOfQuestions):
        typeOfQuestion, l, r = map(int, input().split())
        # first question
        if typeOfQuestion == 1:
            if l == 1:
                print(costsOfStones[r-1])
            else:
                print(costsOfStones[r-1]-costsOfStones[l-1-1])
        # second question
        else:
            if l == 1:
                print(costsOfStonesSorted[r-1])
            else:
                print(costsOfStonesSorted[r-1]-costsOfStonesSorted[l-1-1])

       


    # 6 4 2 7 2 7
    # 0 1 2 3 4 5
    # 2 2 4 6 7 7 


    # 0  1  2  3  4  5 index
    # 4  6  2  7  2  7  >> stones
    # 4  10 12 19 21 28 >> prefixsum
