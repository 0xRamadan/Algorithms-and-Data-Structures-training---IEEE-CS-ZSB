# 
# name: Mahmoud Abdallah Hassan
# link: https://codeforces.com/contest/855/problem/A
# 
# # time complexity: O(n)

def isPossessed(lengthOfList, namesInDiary):
    # main logic
    result = []
    # this is because any first name in namesInDiary won't be possessed
    result.append("NO")
    for i in range(1, lengthOfList):
        if namesInDiary[i] in namesInDiary[:i]:
            result.append("YES")
        else:
            result.append("NO")
    return result





if __name__ == "__main__":
    lengthOfList = int(input())
    
    namesInDiary = []
    for _ in range(lengthOfList):
        namesInDiary.append(str(input()))

    result = isPossessed(lengthOfList, namesInDiary)
    for i in range(lengthOfList):
        print(result[i])