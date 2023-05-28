""" Given an array of n distinct integers, transform the array into a zig zag sequence by permuting the array elements. 

A sequence will be called a zig zag sequence if the first k elements in the sequence are in increasing order and the last k elements are in decreasing order, where k = (n+1)/2. 

You need to find the lexicographically smallest zig zag sequence of the given array. """

""" def findZigZagSequence(a: list, n: int):
    a.sort()
    mid: int = int((n - 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st: int = mid + 1
    ed: int = n - 2

    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    

test_cases: int = int(input())

for cs in range (test_cases):
    n: int = int(input())
    a: list = list(map(int, input().split()))
    findZigZagSequence(a, n)
 """


