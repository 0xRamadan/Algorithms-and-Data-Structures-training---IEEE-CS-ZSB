# name: Mahmoud Abdallah Hassan
# mail: mahmoud.abdallah@ieee-zsb.org
# link: https://codeforces.com/problemset/problem/834/B
# time complexity: O(N)


if __name__ == "__main__":
    
    numberofguests, numberofgaurds = map(int, input().split())
    entrance_doors= input().strip()

    dic = {}
    entrance_doors_set = set()

    for i in range(numberofguests):
       dic[entrance_doors[i]] = i

    # input:
    # AABBB
    # dic:
    # {'A': 1, 'B': 4}


    for i in range(numberofguests):

        entrance_doors_set.add(entrance_doors[i])

        if len(entrance_doors_set) > numberofgaurds:
            print("YES")
            break

        # value of i = value in dic[i] then remove from set
        if i == dic[entrance_doors[i]]:
            entrance_doors_set.remove(entrance_doors[i])


    if len(entrance_doors_set) <= numberofgaurds:
        print("NO")


