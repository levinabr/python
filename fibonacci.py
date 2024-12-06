def fabonacci(no):
    a = 0
    b = 1


    for i in range (no) :
        print(a, end=",")
        a, b = b, b + a
