from stack import Stack

def divBy2(num):
	s = Stack()

	while num > 0:
		rem = num % 2
		s.push(rem)
		num = num // 2

	convertedStr = ""

	while not s.isEmpty():
		temp = s.pop()
		convertedStr = convertedStr + str(temp)

	return convertedStr

def convertBase(num, base):
	digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	s = Stack()
	convertedStr = ""

	while num > 0:
		rem = num % base
		s.push(rem)
		num = num // base

	while not s.isEmpty():
		temp = digits[s.pop()]
		convertedStr = convertedStr + str(temp)
	return convertedStr

print(divBy2(13))
print(convertBase(233,8))
print(convertBase(233,16))
print(convertBase(256,16))
print(convertBase(25,8))
print(convertBase(26,26))