with open("Input/grades.csv") as student:
    students = student.read().splitlines()
    students.pop(0)

max_grade = -1
student_all = []
for i in students:
    if i.strip():
        name,grade = i.split(",")
        grade = int(grade)
        if grade > max_grade:
            max_grade = grade
            student_all = [name]
        elif grade == max_grade:
            student_all.append(name)
        
with open("Output/output21.txt","w") as result:
    result.write(f"eng yuqori  {max_grade} ball olgan talabalar: {', '.join(student_all)}")