# name: Mahmoud Abdallah Hassan
# mail: mahmoud.abdallah@ieee-zsb.org
# link: https://codeforces.com/contest/18/problem/C
# time complexity: O(n)


if __name__ == "__main__":
    stripe_length = int(input())
    square_Values = list(map(int, input().split()))
    
    # create a prefix sum array
    for i in range(1, stripe_length):
        square_Values[i] += square_Values[i-1]


    flag = 0
    for i in range(stripe_length):
        if i != stripe_length - 1 and square_Values[i] == square_Values[stripe_length-1] - square_Values[i]:
            flag += 1

    print(flag)

    # basic logic >> time exceed when it comes to large array
    # flag = 0
    # i = 1
    # while i < len(square_Values):
    #     if sum(square_Values[:i]) == sum(square_Values[i:]):
    #         flag+=1
    #     i += 1
    

    


