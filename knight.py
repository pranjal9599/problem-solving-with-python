from test import Graph, Vertex

def knightGraph(bdSize):
	ktGraph = Graph()
	for row in range(bdSize):
		for col in range(bdSize):
			nodeId = posToNodeId(row, col, bdSize)
			newPositions = genLegalMoves(row,col,bdSize)
			for e in newPositions:
				nid = posToNodeId(e[0],e[1],bdSize)
				ktGraph.addEdge(nodeId,nid)
	return ktGraph

def posToNodeId(row, column, board_size):
	return (row * board_size) + column

def genLegalMoves(x,y,bdSize):
	newMoves = []
	moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
				   ( 1,-2),( 1,2),( 2,-1),( 2,1)]

	# Move offsets a knight can move 2,1 only -1,-2 means up a row
	# and back a column
	# -1,2 means up a row and right to columns
	# ex 12 is passed a possible x,y coordinate is
	# x = 1+(-1), y=2-2
	# x = 0     , y=0 
	# and so on...

	for i in moveOffsets:
		newX = x + i[0]
		newY = y + i[1]
		if legalCoord(newX,bdSize) and \
						legalCoord(newY,bdSize):
			newMoves.append((newX,newY))
	return newMoves

def legalCoord(x,bdSize):
	if x >= 0 and x < bdSize:
		return True
	return False

def knightTour(n,path,u,limit):
	u.setColor('gray')
	path.append(u)
	if n < limit:
		nbrList = list(u.getConnections())
		i = 0
		done = False
		while i < len(nbrList) and not done:
			if nbrList[i].getColor() == 'white':
				done = knightTour(n+1, path, nbrList[i], limit)
			i = i + 1
		if not done: # prepare to backtrack
			path.pop()
			u.setColor('white')
	else:
		done = True
	return done

g = knightGraph(8)
# print(g.getVertices())
