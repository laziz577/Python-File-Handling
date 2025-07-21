with open("Input/grades.csv") as name_grade:
    names = name_grade.read().splitlines()
    names.pop(0)
    
jami = 0
son = 0

for i in names:
    if i.strip():
        name, grade = i.split(",")
        jami += int(grade)
        son += 1

with open("Output/output20.txt","w") as javob:
    if son > 0:
        ortacha = jami / son
        javob.write(f"O'rtacha baho: {round(ortacha,2)}")
    else:
        javob.write("Talaba baho olmagan.")