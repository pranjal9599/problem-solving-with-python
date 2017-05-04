from stack import Stack

def infixToPostfix(infixexpr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	opStack = Stack()
	postfixList = []
	tokenList = infixexpr.split()

	for token in tokenList:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfixList.append(token)
		elif token == '(':
			opStack.push(token)
		elif token == ')':
			topToken = opStack.pop()
			while topToken != '(':
				postfixList.append(topToken)
				topToken = opStack.pop()
		else:
			while (not opStack.isEmpty()) and \
				(prec[opStack.peek()] >= prec[token]):
				postfixList.append(opStack.pop())
			opStack.push(token)

	while not opStack.isEmpty():
		postfixList.append(opStack.pop())
	return " ".join(postfixList)

def doMath(op1, op2, operator):
	if operator == "*":
		return op1 * op2
	elif operator == "/":
		return op1 / op2
	elif operator == "+":
		return op1 + op2
	else:
		return op1 - op2

def evalute(postFixExp):
	opearandStack = Stack()
	postExpList = postFixExp.split()

	for token in postExpList:
		if token in "0123456789":
			opearandStack.push(token)
		else:
			operator2 = opearandStack.pop()
			operator1 = opearandStack.pop()
			val = doMath(operator1, operator2, token)
			opearandStack.push(val)
	return opearandStack.pop()

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))