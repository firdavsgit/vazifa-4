
greet_people = ["Frank", "Angela", "Joe"]
ln = len(greet_people)


if ln == 1:
    print(f"Hello {greet_people[0]}")

elif ln == 2:
    print(f"Hello {greet_people[0]}, Hello {greet_people[1]}")

elif ln == 3:
    print(f"Hello {greet_people[0]}, Hello {greet_people[1]}, Hello {greet_people[2]}")

else:
    print("Error")

