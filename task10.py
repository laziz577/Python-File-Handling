f01 = open('Input/numbers.txt')
content = f01.read()
f01.close()


numbers = list(map(int, content.split()))
tartiblangan_ruyxat= sorted(numbers)


f02 = open('output/sorted_numbers.txt','w')
f02.write(str(tartiblangan_ruyxat))
f02.close()