
num = int(input("enter number:"))

list =[1,4,2,6,3,7,8,9,5]
list.sort()
print(list)

def find(number, lst):
    lst.sort()
    n = lst[number]
    return n
print(find(num,list))




