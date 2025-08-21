N = int(input("Enter a number: "))

i = 1
while(i<N):
    if(N%i==0): # i is factor
        print(i)
    i += 1