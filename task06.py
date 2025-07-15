f01 = open('Input/numbers.txt')
content = f01.read()
f01.close()

numbers = list(map(int, content.split()))
toq_sonlar= list(filter(lambda n: n % 2 == 1, numbers))

f02 = open('odd_numbers.txt',"x")
f02.write(str(toq_sonlar))
f02.close()
