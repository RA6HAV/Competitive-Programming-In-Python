# Q5. Read a number check if it is divisible by 7 or its last digit is 5.

num = int(input("Enter a number: "))
if(num % 7 == 0 and  num % 10 == 5):
    {
       print("This number is divisible by 7. \nLast digit of this number is 5.")
    }
else:{
    print("This number is not divisible by 7. \nLast digit of this number is not 5.")
}
