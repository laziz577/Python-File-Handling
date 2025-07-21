with open("Input/grades.csv") as student:
    students = student.read().splitlines()
    students.pop(0)

all_student = []
for i in students:
    if i.strip():
        name,grade = i.split(",")
        grade = int(grade)
        if grade == 5:
            all_student.append(name)
        
with open("Output/high_scores.csv","w") as javob:
    javob.write("5 baho olgan talabalar: " + ",".join(all_student))