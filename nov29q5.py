"""Recursive function to multiply two positive numbers"""
def num(num1,num2):
    if num2==1 :
        return num1
    if num1 and num2 < 0:
        print("invalid input")
    else:
        return num1 +num(num1,num2-1)


n1 = int(input("Enter a number = "))
n2 = int(input("Enter another number = "))
print("Multiplication of the numbers using recursive function is = ",num(n1,n2))
