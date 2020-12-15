# name: Mahmoud Abdallah Hassan
# mail: mahmoud.abdallah@ieee-zsb.org
# link: https://codeforces.com/problemset/problem/141/A
# time complexity: O(1) 

def canBePremuted(guestName, hostName, letter):

    myletter = str(guestName) + str(hostName)
    myletter = sorted(myletter) # become list

    letter = sorted(letter)

    if letter == myletter:
        print("YES")
    else:
        print("NO")



if __name__ == "__main__":
    guestName = input().strip()
    hostName = input().strip()
    letter = input().strip()
    canBePremuted(guestName, hostName, letter)

