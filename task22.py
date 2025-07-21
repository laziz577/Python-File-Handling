with open("Input/grades.csv") as student:
    students = student.read().splitlines()
    students.pop(0)

soni = 0
for i in students:
    if i.strip():
        name,grade = i.split(",")
        grade = int(grade)
        if grade == 5:
            soni += 1
        
with open("Output/output22.txt","w") as javob:
    javob.write(f"5 baho olgan talabalar soni: {soni}")