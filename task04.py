f01 = open('Input/numbers.txt')
content = f01.read()
f01.close()

numbers = list(map(int,content.split()))
juft_sonlar = list(filter(lambda n: n % 2 == 0,numbers))

f02 = open('Output/output04.txt','w')
f02.write(str(juft_sonlar))
f02.close()
