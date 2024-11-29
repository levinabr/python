"""description = Recursive function to add two positive numbers."""

def add(num1,num2):
    if num2==0:
        return num1
    if num1 and num2 < 0:
        print("invalid input")
    else :
        return add(num1+1,num2-1)
n1 = int(input("Input a number = "))
n2 = int (input("Input another number"))
print("Sum of the numbers using recursive function is = ",add(n1,n2))
