# my Welcome back problem
# Problem link: https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
# problem name: Subarray Division / birthday Chocolate
# CS21-Science-Day-27
# github: @RaymondReddigton

def birthday(s, d, m):
    # Write your code here
    count = 0
    TotalScoreOnSquares = sum(s[:m])
    
    if TotalScoreOnSquares == d:
        count +=1
    
    for i in range(m, len(s)):
        TotalScoreOnSquares += s[i]
        TotalScoreOnSquares -= s[i-m]
        if TotalScoreOnSquares == d:
            count += 1
            
    return count

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)
    print(result)
