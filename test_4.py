
rows = int(input("Enter number of rows : "))
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(end = ' ')
    for k in range(1, 2 * i):
        if k == 1 or k == i * 2 - 1:          
            print('*', end = '')
        else:
            print(' ', end = '')
    print()


for i in range(rows - 1, 0, -1):
    for j in range(1, rows - i + 1):
        print(' ', end = '')
    for k in range(1, 2 * i):
        if k == 1 or k == i * 2 - 1:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
