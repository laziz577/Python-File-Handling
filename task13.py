f01= open("input/students.txt", 'r')
content = f01.read()
f01.close()

names = list(map(str,content.split()))
tartiblangan_ismlar = sorted(names,key = lambda ism:ism)


f02 = open("output/output13.txt", 'w')
f02.write(str(tartiblangan_ismlar))
f02.close()