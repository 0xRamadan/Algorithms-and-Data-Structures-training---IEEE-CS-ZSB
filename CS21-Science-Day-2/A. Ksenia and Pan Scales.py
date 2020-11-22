def check(l, r):
    if len(left_scale) == len(right_scale):
            print(''.join(left_scale)+'|'+''.join(right_scale))
    else:
        print('Impossible')

if __name__ == "__main__":
    l = list(map(str, input().rstrip()))
    # finding the delimiter
    delimiter = l.index('|')
    # slicing to left list and right list
    left_scale = l[:delimiter]
    right_scale = l[delimiter+1:]
    # taking the weight from the user
    weight = list(map(str, input().rstrip()))
    # putting the weight one by one into left or right
    for i in weight:
        if  len(left_scale) > len(right_scale):
            right_scale.append(i)
        else:
            left_scale.append(i)
    # a func to check if The scales is in equilibrium
    check(left_scale, right_scale)