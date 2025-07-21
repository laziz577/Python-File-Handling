with open("Input/grades.csv") as student:
    students = student.read().splitlines()
    students.pop(0)

soni5= 0
soni4= 0
soni3= 0
soni0= 0


for i in students:
    
    if i.strip():
        name,grade = i.split(",")
        grade = int(grade)
        
        if grade == 5:
            soni5 += 1
        elif grade == 4:
            soni4 += 1
        elif grade == 3:
            soni3 += 1
        else:
            soni0 += 1
           
             
with open("Output/output23.txt","w") as javob:
    javob.write(
    f"5 baho - {soni5} marta\n"
    f"4 baho - {soni4} marta\n"
    f"3 baho - {soni3} marta\n"
    f"{soni0} ta talaba baho ololmagan\n"
)