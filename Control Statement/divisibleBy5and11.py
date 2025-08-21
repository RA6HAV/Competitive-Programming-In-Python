# Q5. Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or not.

num = int(input("Enter a number: "))

if(num%5==0 and num%11==0):{
    print(num,"is divisible by 5 and 11.")
}
else:{
        print(num,"is not divisible by 5 and 11.")
}