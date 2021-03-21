# name: Mahmoud Abdallah Hassan
# mail: mahmoud.abdallah@ieee-zsb.org
# link: https://codeforces.com/problemset/problem/579/A
# time complexity: O(n)

if __name__ == "__main__":
    n = bin(int(input()))

    print(n.count('1'))

    '''
    another solution

    b = int(input())
    counter =0
    while b:
        # reference with one to check last right bit one or zero.
        if b&1:
            counter += 1
        # shift last bit, which means removes last bit
        b = b >> 1
        
    print(counter)

    '''