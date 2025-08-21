# Q4. Check if its divisible by 3 and its last digit is 4.

num = int(input("Enter a number: "))
if(num % 3 == 0 and  num % 10 == 4):
    {
       print("This number is divisible by 3. \nLast digit of this number is 4.")
    }
else:{
    print("This number is not divisible by 3. \nLast digit of this number is not 4.")
}
