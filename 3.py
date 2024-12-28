for x in range(4):
    for y in range(5):
        print("*",end='')
    print()




for row in range(4):
    for col in range(row+1):
        print("*",end='')
    print()




for row in range(5):
    for col in range(5-row):
        print("*",end='')
    print()



for row in range(4):
    for col in range(row+1):
        print(row,end='')
    print()