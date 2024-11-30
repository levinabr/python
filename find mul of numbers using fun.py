def numbers(num):
    mul = 1
    for i in num:
        mul=mul*i
    return mul
number = []
n = int(input("enter the number of element"))
for x in range(n):
    element = int(input("Enter the elements"))
    number.append(element)
print("sum of elements is = ",numbers(number))
