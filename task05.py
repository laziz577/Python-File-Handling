f01 = open('Input/numbers.txt')
content = f01.read()
f01.close()


numbers = list(map(int, content.split()))
jami = sum(numbers)
average = jami/len(numbers)

f02 = open('Output/output05.txt','w')
f02.write(f'Urtacha son: {average}')
f02.close()