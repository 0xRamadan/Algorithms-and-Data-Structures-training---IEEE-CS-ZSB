# taking input from the user as a string
s = input()
while s:
    last1 = -1
    count_1s = 0            # 01234 # length = 5
    for i in range(len(s)): # 10100
        if s[i] == '1':     # 43210
            if last1 == -1:
                last1 = i
            count_1s += 1
        
    # special handling zero 
    if count_1s == 0:
        print('0')
        break

    last1 = len(s) - last1 - 1

    # handling odd power
    if last1 % 2 == 1:
        last1 += 1
        count_1s = 0

    last1 = last1 / 2

    # check if there are ones
    if count_1s > 1:
        last1 += 1
    
    print(int(last1))
    break