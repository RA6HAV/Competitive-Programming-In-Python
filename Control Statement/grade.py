# Accept the percentage from the user and display the grade according to criteria.

percentage = float(input("Enter percentage: "))

if (percentage < 0 or percentage > 100):
    print("Invalid percentage! Please enter a value between 0 and 100.")
elif (percentage >= 90):
    print("Grade: A+")
elif (percentage >= 80):
    print("Grade: A")
elif (percentage >= 70):
    print("Grade: B")
elif (percentage >= 60):
    print("Grade: C")
elif (percentage >= 50):
    print("Grade: D")
elif (percentage >= 40):
    print("Grade: E")
else:
    print("Grade: Fail")