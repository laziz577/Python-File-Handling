f01 = open('Input/numbers.txt')
content = f01.read()
f01.close()

numbers = list(map(int, content.split()))
beshga_karrali = list(filter(lambda n: n % 5 == 0, numbers))

f02 = open('Output/output08.txt',"w")
f02.write(str(beshga_karrali))
f02.close()