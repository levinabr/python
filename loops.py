num = int(input("Enter a number \n"))
Sum = 0
x = num
while num>0 :
    r = num%10

    Sum = Sum + pow(r,3)
    num = num//10
if Sum == x :
  print(x,"\tis  a armstrong number")
else :
    print(x,"\tis not a armstrong number")
