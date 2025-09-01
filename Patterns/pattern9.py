n = 4
m = 4

for i in range(1,n+1):
    for j in range(1,m+1):
        if(i==1 or i==4):
            print("*",end=" ")
        elif(j==1 or j==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
