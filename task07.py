f01 = open('Input/numbers.txt')
content = f01.read()
f01.close()

numbers = list(map(int, content.split()))
kvadrat_sonlar = list(map(lambda son:son ** 2, numbers))

f02 = open('Output/output07.txt',"w")
f02.write(str(kvadrat_sonlar))
f02.close()