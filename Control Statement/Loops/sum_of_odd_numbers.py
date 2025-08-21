# Q7. Take an integer A as input. You have to print the sum of all odd numbers in the range [1, A].

A = int(input("Enter a number: "))

odd_sum = 0

for i in range(1, A + 1, 2):
    odd_sum += i
print(odd_sum)