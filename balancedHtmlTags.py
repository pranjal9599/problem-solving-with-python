import re
from stack import Stack

def getTag(tag):
	tag = tag.replace('<', '')
	tag = tag.replace('>', '')
	tag = tag.replace('/', '')
	return tag

def checkBalanced(doc):
	html_string = open(doc)
	html_string = html_string.read()
	balanced = True
	matches = re.findall('<.*?>', html_string)
	tags = Stack()
	for tag in matches:
		if (tag[1] == '/'):
			closing = getTag(tag)
			opening = getTag(tags.pop())
			if not opening == closing:
				balanced = False
		else:
			tags.push(tag)

	if not tags.isEmpty():
		balanced = False

	return balanced

print(checkBalanced('check.html'))
print(checkBalanced('check1.html'))
print(checkBalanced('check3.html'))
