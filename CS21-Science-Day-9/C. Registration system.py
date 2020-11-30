# 
# name: Mahmoud Abdallah Hassan
# link: https://codeforces.com/contest/4/problem/C
# 
# time complexity: O(n)

if __name__ == "__main__":
    
    n = int(input())
 
    database = {}
    for i in range(n):
        username = input()
        
        # check if username is in the dictionary
        if username in database:
            # note that the value of non-found username is none, So there will be no value.
            print(username+str(database[username]))
            database[username] += 1
        else:
            print("OK")
            database[username] = 1