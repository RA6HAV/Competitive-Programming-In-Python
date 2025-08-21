# Q1. Write a program to takes a positive integer N as input the from user and print all the natural numbers from 1 to N, with each number followed by a space.

num = int(input("Enter a positive number: "))
i = 1
while i  <= num:
    print(i,end=" ")
    i = i + 1