'''
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
'''

n = 6
for i in range(1, n):
    for j in range(1, i + 1):
        print(n - i, end=' ')
    print()
