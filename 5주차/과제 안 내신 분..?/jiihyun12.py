students = []
for i in range(1, 31):
    students.append(i)
    
for _ in range(28):
    input_students = int(input())
    students.remove(input_students)
students.sort()

for students_numbers in students:
    print(students_numbers)    
