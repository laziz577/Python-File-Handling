f01 = open('Input/numbers.txt')
content = f01.read()
f01.close()

total = max(map(int,content.split()))


f02 = open('Output/output03.txt','w')
f02.write(f"Jami:{total}")
f02.close()
