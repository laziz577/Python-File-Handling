f1 = open('Input/numbers.txt')
content = f1.read()
f1.close()

numbers = list(map(int, content.split()))
beshga_karrali = list(filter(lambda n: n % 5 == 0, numbers))

f2 = open('Output/output08.txt',"w")
f2.write(str(beshga_karrali))
f2.close()