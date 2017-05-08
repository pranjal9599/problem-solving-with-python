class OrdererList:
	def __init__(self):
		self.head = None

	def search(self,item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()
		return found

	def add(self,item):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current	
				current = current.getNext()

			temp = Node(item)
			if previous == None: #head in this case item added is smallest
				temp.setNext(self.head)
				self.head = temp
			else:
				temp.setNext(current)
				previous.setNext(temp)

	def remove(self,item):
		current = self.head
		previous = None
		stop = False
		if current.getData() < item:
			stop = True
