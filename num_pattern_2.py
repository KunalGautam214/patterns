'''
2
3 4
4 5 6
5 6 7 8
6 7 8 9 10
'''

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i + j, end=' ')
    print()
