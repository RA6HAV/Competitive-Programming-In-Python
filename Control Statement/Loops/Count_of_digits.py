# Q8. Take an integer N as input and print the count of digits of that number.

N = int(input("Enter a number: "))

count = len(str(abs(N)))

print("Number of digits: ", count)
