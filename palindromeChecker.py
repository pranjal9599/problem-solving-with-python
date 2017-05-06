from deque import Deque

def checker(string):
	chardeque = Deque()

	for ch in string:
		chardeque.addRear(ch)

	stillEqual = True

	while chardeque.size() > 1 and stillEqual:
		first = chardeque.removeFront()
		last = chardeque.removeRear()	
		if first != last:
			stillEqual = False

	return stillEqual

print(checker("madam"))