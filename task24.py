with open("Input/grades.csv") as name_grade:
    names = name_grade.read().splitlines()
    names.pop(0)


jami = 0
soni = 0
students = []

for i in names:
    if i.strip():
        name, grade = i.split(",")
        grade = int(grade)
        students.append((name, grade))
        jami += grade
        soni += 1

urtacha = jami / soni


baland_olganlar = []
for name, grade in students:
    if grade > urtacha:
        baland_olganlar.append(f"{name} - {grade}")


with open("Output/output24.txt", "w") as javob:
    javob.write(
        f"urtacha ball: {urtacha} baldan baland olgan talabalar: {baland_olganlar}"
    )