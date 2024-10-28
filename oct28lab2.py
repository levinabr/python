temp = int(input("enter the temperature\n"))
print("Enter unit of your temperature")
print("1.\t Celsius  ")
print("2.\tFahrenheit")
print("3.\texit()")
choice = int(input("Enter Your Unit Of Temperature \n"))
while True :
    if choice ==1:
        f = (temp * 9 / 5) + 32
        print(f, "is the converted temperature")
        break
    elif choice ==2 :
        c = 9 / 5 * (temp - 32)
        print(c, "is the converted temperature")
        break
    elif choice ==3 :
        break