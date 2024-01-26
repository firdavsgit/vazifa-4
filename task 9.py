list = [3, 2, 5]
list2 = [5,3, 7, 9, 2]
def find(lst, lst2):
    for x in lst:
        if x in lst2:
            return True
        else:
             return False

print(find(list,list2))