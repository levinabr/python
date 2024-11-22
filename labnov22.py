list_1 = [1,2,3,4,5,6,7,8,9]
list_2 = [10,11,12,13,14,15,16]
list_3 = list_1+list_2
list_4 = []
list_5 = []
print(f"The First List is \n{list_1}")
print(f"The Second List is \n{list_2}")
print(f"Before sorting \n{list_3}")
for number in list_3 :
    if number%2== 0 :
        list_4.append(number)

    else :
        list_5.append(number)
print(f"The list after sorting is \n{list_4+list_5}")