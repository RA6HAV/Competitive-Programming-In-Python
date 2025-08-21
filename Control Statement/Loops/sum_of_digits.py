# Q9. Take an integer N as input. Your task is to calculate and print the sum of the digits of the given number N.

n = int(input("Enter a number: "))

n = abs(n)

digit_sum = 0
while n > 0:
    digit_sum += n % 10
    n //= 10

print("Sum of digits: ", digit_sum)