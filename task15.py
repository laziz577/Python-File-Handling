f01= open("input/students.txt", 'r')
content = f01.read()
f01.close()

names = content.split()
ishtirokchilar = map(lambda ism:ism + " - " + str(len(ism)) + "harfdan", names)



f02 = open("Output/output15.txt", 'w')
f02.write('\n'.join(ishtirokchilar))
f02.close()