import sys



# add Payload for data
class Node :
	
	def __init__(self, level) :
		self.level = level
		self.payload = ""
		self.leftChild = None
		self.rightChild = None
			

	def __str__(self) :
		return 	"level={self.level}, payload={self.payload} ".format(self=self) 

	
	def insertLeft(self, level) :	
		if level < minLevel 
			print('error in insertLeft, requested level is: ' + str(level))
			sys.exit()
			
		self.leftChild = Node(level)			

			
	def insertRight(self, level) :
		if level < minLevel 
			print('error in insertRight, requested level is: ' + str(level))
			sys.exit()
				
		self.rightChild = Node(level)
	
		

	def traverse(self):
		print(self.key)
		if self.leftChild:
			self.leftChild.traverse()
		if self.rightChild:
			self.rightChild.traverse()      


	def isAllocated(self) :
		if self.payload == "" :
			return False
		else :
			return True
			
	def isRightLevel(self, level) :
		if self.level == level :
			return True
		else :
			return False
			
	def isLeaf(self) :
		if self.leftChild is None :
			return True
		else :
			return False
			

'''
class Node :
	
	def __init__( self, parent, capacity=1024, level=0, left=None, right=None, size=0 ) :
		self.capacity = capacity
		self.level = level
		self.left = left
		self.right = right
		self.size = size
		self.parent = parent
		#self.name = name
'''	
	
		


def findLevel( u, size ) :
	
	if 2**(u-1) < size <= 2**u : 
		#if the size is between the two levels, return this level
		return u
		
	else : 	
		# if the lower limit is reached, return this level
		if u == minLevel :
			return u
		# recursively descend levels
		return findLevel(u-1, size)


def addNodeToTree(tree, node) :
	if tree.isAllocated() :
		print ('allocated, returning False')
		return False
	
	if tree.isRightLevel(node.level) :
		if tree.isLeaf() :
			print('call allocate')
			return True
		else :
			return False
	
	if tree.isLeaf() :
		print('create children')
		tree.insertLeft(tree.level - 1)
		tree.insertRight(tree.level - 1)
		
	if addNodeToTree(tree.leftChild, node) == True :
		return True
	else 
		if addNodeToTree(tree.rightChild, node) == True :
			return True
	return False
		


def addNodeToTree_old(tree,  node) :
	# if node is free
	if not tree.payload :
		
		if tree.level == node.level :
			print('insert here')
			return node
		else :
			print('descend a level')
			tree.insertLeft()
			tree.insertRight()
			
	else :
		print('tree full')

def printTree( tree ) :
	print(tree)

# set some parameters
maxBlock = 8
maxLevel = 3 
minLevel = 1

u = maxLevel
size = 8

if size > maxBlock :
	print('size is too big')
	sys.exit()
	
level = findLevel(u,size) 

n1 = Node(3)
n1.payload = 'Ben'

n2 = Node(3)
n2.payload = 'Jen'

n3 = Node(2)
n3.payload = 'Finn'

n4 = Node(2)
n4.payload = 'El'



# start a tree
tree = Node(3)
print(tree)

tree = addNodeToTree(tree, n1)
printTree(tree)
tree = addNodeToTree(tree, n2)
printTree(tree)




