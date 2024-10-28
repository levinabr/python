balance_amount=1000
while True:
    print("1.\t Check balance ")
    print("2.\tdeposit money")
    print("3.\twithdraw money")
    print("4.\texit()")
    choice = float(input("Enter your choice \n"))
    if choice == 1:
        print(f"your balance is {balance_amount} \n")
    elif choice==2:
        new = float (input("Enter the deposited money \n"))
        balance_amount = new+balance_amount
        print(f" Your current balance is = {balance_amount} \n")
    elif choice ==3 :
        draw = float(input("Enter the money which you want to withdraw \n"))
        if draw>balance_amount :
            print("Invalid Withdrawal \n")
        else :
            balance_amount = balance_amount-draw
        print(f"YOur current balance is = {balance_amount} \n")


    elif choice ==4:
        break
    else :
        print("Invalid Input")

