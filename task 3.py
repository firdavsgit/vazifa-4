list = [1, 4, 4, 4, 4, 4, 3, 2, 1, 2]
list2 = []
def set(lst,lst2):
    for x in lst:
        if x not in lst2:
            lst2.append(x)
            lst2.sort()
    return lst2

print(set(list,list2))