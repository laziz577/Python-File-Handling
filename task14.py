f01= open("input/students.txt", 'r')
content = f01.read()
f01.close()

names = list(map(str,content.split()))
teskari_tartib = sorted(names,key = lambda ism:ism,reverse=True)


f02 = open("output/output14.txt", 'w')
f02.write('\n'.join(teskari_tartib))
f02.close()