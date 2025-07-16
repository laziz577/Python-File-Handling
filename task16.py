f01= open("input/students.txt", 'r')
content = f01.read()
f01.close()

ism = []
for i in content.split():
    if len(i) > 5:
        ism.append(i)


f02 = open("Output/output16.txt", 'w')
f02.write(f"5 dan katta ismlar:{ism}")
f02.close()