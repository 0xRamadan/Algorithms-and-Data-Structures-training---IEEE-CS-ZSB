# name: Mahmoud Abdallah Hassan
# mail: mahmoud.abdallah@ieee-zsb.org
# link: https://codeforces.com/contest/1025/problem/A
# time complexity: O(n)

def can_be_recolored(colors, numberOfColors):
    # prepocessing
    # e.g: ord(j) = 106  >> length of freq_array = 106 - 96 = 10
    frequency_array = [0 for i in range(ord(max(colors)) - 96)]
    for color in colors:
        frequency_array[ord(color)-97] += 1
    
    flag = 0 
    for color in frequency_array:
        if color > 1 or numberOfColors == 1:
            flag += 1
            break
    return flag


if __name__ == "__main__":
    numbersOfPuppies = int(input())
    colorsOfPuppies = input().strip()
   
    if can_be_recolored(colorsOfPuppies, numbersOfPuppies):
        print("YES")
    else:
        print("NO")