# Write a program to input three numbers and print the minimum among them.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if (num1<num2 and num1<num3):
    	print("num1 is min")
elif(num2<num3):
    	print("num2 is min")
else:
	print("num3 is min")