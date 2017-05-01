import operator

class Stack:
    def __init__(self):
        self.items = []
        self.size = -1

    def push(self, data):
        self.size = self.size+1
        self.items.append(data)
        
    def pop(self):
        self.size = self.size-1
        return self.items.pop()

    def size(self):
        return self.size

class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.rightNode = None
        self.leftNode = None

    def insertLeft(self, what):
        if self.leftNode == None:
            self.leftNode = BinaryTree(what)
        else:
            t = BinaryTree(what)
            t.leftNode = self.leftNode
            self.leftNode = t

    def insertRight(self, what):
        if self.rightNode == None:
            self.rightNode = BinaryTree(what)
        else:
            t = BinaryTree(what)
            t.Node = self.rightNode
            self.rightNode = t

    def getLeftChild(self):
        return self.leftNode

    def getRightChild(self):
        return self.rightNode

    def getRootVal(self):
        return self.root

    def setRootVal(self, newRoot):
        self.root = newRoot

        
def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i == ')':
            currentTree = pStack.pop()
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        else:
            raise ValueError
    return eTree

def evalute(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evalute(leftC), evalute(rightC))
    else:
        return parseTree.getRootVal()
    

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(evalute(pt))
