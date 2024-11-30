def reverse_string(String):
    reverse = ""
    for i in String:
        reverse = i + reverse
    return reverse

String=input("enter the string:")
print(reverse_string(String))
