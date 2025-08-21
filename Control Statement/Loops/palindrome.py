# Q10. You are given an integer A as input, and you need to determine whether it is a palindrome or not

A = int(input("Enter a number: "))

original = A
reverse = 0
temp = abs(A)

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if reverse == abs(original):
    print("Palindrome")
else:
    print("Not Palindrome")