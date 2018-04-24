import sys



# add Payload for data
class BinaryTree :
	
	def __init__(self, rootObj) :
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None	

	
	def insertLeft(self, newNode) :	
		# if no exisiting left child, just create new and insert
		if self.leftChild == None :
			self.leftChild = BinaryTree(newNode)			
		else:
			# i don't think there is a case for else as we domt want to move anything
			print('insertLeft - else, shouldnt be here!')
			#t = BinaryTree(newNode)
			#t.leftChild = self.leftChild
			#self.leftChild = t 
			
	def insertRight(self, newNode) :
		# if no existing right child, creare newand insert
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			print('insertRight - else, shouldnt be here!')
			#t = BinaryTree(newNode)
			#t.rightChild = self.rightChild
			#self.rightChild = t
			
	def getRightChild(self):
		return self.rightChild
	
	def getLeftChild(self):
		return self.leftChild
	
	def setRootVal(self,obj):
		self.key = obj
	
	def getRootVal(self):
		return self.key
		

	def traverse(self):
		print(self.key)
		if self.leftChild:
			self.leftChild.traverse()
		if self.rightChild:
			self.rightChild.traverse()      


class Node :
	
	def __init__( self, parent, capacity=1024, level=0, left=None, right=None, size=0 ) :
		self.capacity = capacity
		self.level = level
		self.left = left
		self.right = right
		self.size = size
		self.parent = parent
		#self.name = name
		
	def __str__(self) :
		retString = (	"capacity={self.capacity}, size={self.size} "
									"level={self.level},".format(self=self) )

		if self.parent is not None :
			retString += ", parent.size={self.parent.size}".format(self=self)
		return retString
		


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
print('size = ' + str(size) + ',  looking for level = ' + str(level))

# start a tree
tree = Node(None, maxBlock, maxLevel)
print(str(tree))

# add size to tree
if level == tree.level :
	tree.size = size
	print(tree)

else :
	tree




