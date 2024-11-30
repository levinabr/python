def largest_of (a,b,c):
    if a<b>c:
        return b
    elif  b<c>a :
        return c
    elif c<a>b :
        return a
A = int(input("Enter a number (n1) = "))
B = int(input("Enter a number (n2) = "))
C = int(input("Enter a number (n3) = "))
print(f"The Largest of these numbers are =",largest_of(A,B,C))
