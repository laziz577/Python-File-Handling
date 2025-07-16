f01= open("input/students.txt", 'r')
content = f01.read()
f01.close()

names = list(map(str,content.split()))
ismlar_soni = len(names)



f02 = open("output/output12.txt", 'w')
f02.write(str(ismlar_soni))
f02.close()