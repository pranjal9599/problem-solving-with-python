class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext

class LinkedList:
	def __init__(self):
		self.head = None
		self.last = None

	def isEmpty(self):
		return self.head == None

	def add(self,item):
		temp = Node(item)

		if self.head == None:
			self.last = temp

		temp.setNext(self.head)
		self.head = temp

	def size(self):
		temp = self.head
		size = 0
		while temp:
			temp = temp.getNext()
			size = size + 1
		return size

	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None: # in head case previous is None
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def append(self,item):
		lastItem = self.head
		temp = self.head
		while temp:
			lastItem = temp
			temp = temp.getNext()
		node = Node(item)
		lastItem.setNext(node)

	def appendMod(self, item):
		if self.last:
			temp = Node(item)
			self.last.setNext(temp)

	def print(self):
		temp = self.head
		while temp:
			print(temp.getData())
			temp = temp.getNext()

list = LinkedList()
list.add(2)
list.add(10)
list.add(20)
list.add(30)
list.add(40)
list.add(50)
list.add(60)
list.add(70)
list.appendMod(100)
list.print()