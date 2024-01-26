
list = [1, 4, 4, 4, 4, 4, 3, 2, 1, 2]
list2 = []

for x in list:
    if x not in list2:
        list2.append(x)
        list2.sort()
print(list2)







