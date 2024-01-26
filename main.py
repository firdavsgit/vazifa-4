names = ["BMW", "Mers", "Chevrolet", "Tahoe", "Ford"]
first = []

def find_secret(cars,lst):
    for x in cars:
        lst.append(x[0])
        lst.sort()
    j = "".join(lst)
    return j
print(find_secret(names,first))








