
def hesaplama(x, y, islem):

    if islem not in '+-/*':
        return 'Choose operator: "+, -, *, /"!'

    if islem == '+':
        return(str(x) + ' ' + islem + ' ' + str(y) + ' = ' + str(x + y))
    if islem == '-':
        return(str(x) + ' ' + islem + ' ' + str(y) + ' = ' + str(x - y))
    if islem == '*':
        return(str(x) + ' ' + islem + ' ' + str(y) + ' = ' + str(x * y))
    if islem == '/':
        return(str(x) + ' ' + islem + ' ' + str(y) + ' = ' + str(x / y))

while True:

	x = int(input('ilk sayıyı girin: '))
	y = int(input('ikinci sayıyı girin: '))
	ops = input("bunlardan birini seçin +, -, *, / ")

	print(hesaplama(x, y, islem = ops))