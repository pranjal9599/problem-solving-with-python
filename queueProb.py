from queue import Queue

def hotPotato(namelist, num):
	simqueue = Queue()
	for name in namelist:
		simqueue.enqueue(name)

	while simqueue.size() > 1:
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())

		simqueue.dequeue()

	return simqueue.dequeue()

print(hotPotato(["Bill","Steve","Musk","Feyman","Kalam","Do ra me","joji"],7))