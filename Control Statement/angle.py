# Q7. Read three angles of triangles and determine their types(Right triangle, Obtusetriangle, Acute triangle).

angle1 = int(input("Enter 1st angle: "))
angle2 = int(input("Enter 2nd angle: "))
angle3 = int(input("Enter 3rd angle: "))

if (angle1 == 90 or angle2 == 90 or angle3 == 90):{
    print("This is a right triangle")
}
elif(angle1>90 or angle2>90 or angle3>90):{
    print("This is a Obtuse triangle")
}
else:{
    print("This is a Acute triangle.")
}
