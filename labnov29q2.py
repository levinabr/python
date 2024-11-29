"""
description= A program that accepts the lengths of three sides of a triangle as inputs.
 The program should output  the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle,
the square of one side equals the sum of the squares of the other two sides). Implement using functions.
"""
def triangle(sides):
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        return True
    return False
sides = []
num1 = int(input("Enter side 1"))
num2 = int(input("Enter side 2"))
num3 = int(input("Enter side 3"))
sides.append(num1)
sides.append(num2)
sides.append(num3)
if triangle(sides):
    print("The given sides are part of Right Triangle")
else :
    print("the given side are not part of Right Triangle")