# Student Data Management Using Dictionary, Tuple, and List

student1 = (101, "Rahul", "Computer Science", 85)
student2 = (102, "Priya", "Information Technology", 90)
student3 = (103, "Amit", "Electronics", 78)

students = {
    student1[0]: student1,
    student2[0]: student2,
    student3[0]: student3
}

print("Initial Student Records:")
print(students)

new_student = (104, "Sneha", "Mechanical", 88)
students[new_student[0]] = new_student

print("\nAfter Adding New Student:")
print(students)

del students[102]

print("\nAfter Deleting Student with Roll Number 102:")
print(students)

updated_student = (103, "Amit Kumar", "Electronics", 82)
students[103] = updated_student

print("\nAfter Updating Student with Roll Number 103:")
print(students)

student_list = list(students.values())

print("\nFinal Student Records:")
for student in student_list:
    print("Roll Number:", student[0])
    print("Name:", student[1])
    print("Branch:", student[2])
    print("Marks:", student[3])
    print()
