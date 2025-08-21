# Q12. You are given two integers A and B. You have to find the value of A^B.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

ans = 1
for i in range(b):
    ans = ans*a
    print(ans,end=" ")