# name: Mahmoud Abdallah Hassan
# mail: mahmoud.abdallah@ieee-zsb.org
# link: https://codeforces.com/problemset/problem/368/B
# time complexity: O(n) 


if __name__ == "__main__":
    a_length, m_length = map(int, input().split())
    a_array = list(map(int, input().split()))
    a_set = set()
    
    freq = []
    # reverse iteration
    for i in range(a_length-1, -1, -1):
        a_set.add(a_array[i])
        freq.append(len(a_set))
    # print(freq)  >> [1, 2, 3, 4, 5, 6, 6, 6, 6, 6]
    for _ in range(m_length):
        print(freq[-1 * int(input())])       