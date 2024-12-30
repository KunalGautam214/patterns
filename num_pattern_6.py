'''
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''

n = 6
for i in range(1, n):
    for j in range(1, i + 1):
        print(n - j, end=' ')
    print()



