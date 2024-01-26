get_student_names = {
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}

list = []
def return_names(get_student):
    for value in get_student.values():
        list.append(value)
        list.sort()
    return list

print(return_names(get_student_names))