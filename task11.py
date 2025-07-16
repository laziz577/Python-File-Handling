f01= open("input/students.txt", 'r')
content = f01.read()
f01.close()

f02 = open("output/output11.txt", 'w')
f02.write(content)
f02.close()