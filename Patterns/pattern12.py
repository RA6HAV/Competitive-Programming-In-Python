rows = 5
for i in range(1, rows + 1):       
    num = 1
    for j in range(1, i + 1):      
        if j % 2 != 0:             
            print(num, end=" ")
            num += 2
        else:                      
            print("*", end=" ")
    print()