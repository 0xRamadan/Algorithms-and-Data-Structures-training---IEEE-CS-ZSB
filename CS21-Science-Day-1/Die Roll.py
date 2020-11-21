from fractions import Fraction

l = list(map(int, input().split()))
max_n = max(l)
p = Fraction(6-(max_n-1))/6
if p == 1:
    print('1/1')
elif p == 'zero':
    print('0/1')
else:
    print(p)
input('press enter to exit...')
