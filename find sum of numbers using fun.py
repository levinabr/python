def numbers(num):
   sum = 0
   for i in num:
       sum= sum+i
   return sum
num = []
n = int(input("Enter the number of elements"))
for x in range(n):
    element = int(input("Enter the elements"))
    num.append(element)
print("sum of elements is = ",numbers(num))