name = input("enter name:").title()

with open("Input/students.txt") as student:
    students = student.read()
    
    if name in students:
        result = f"{name} ismi mavjud."
    else:
        result = f"{name} ismi mavjud emas"
        
with open("Output/output18.txt","w") as javob:
    javob.write(f"{result}")