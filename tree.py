import node


class Tree:

	# initialise to empty
	def __init__(self, maxLevel):

		# define a top to the tree
		self.topNode = node.Node(maxLevel)
		self.topFreeLevel = maxLevel
		self.topNode.right = True

	def addNode(self, node, newNode):
		if node.isAllocated():
			return False

		if node.isRightLevel(newNode.level):
			if node.isLeaf():
				node.payload = newNode.payload
				return True

			else:
				return False

		if node.isLeaf():
			node.insertLeft(node.level - 1)
			node.insertRight(node.level - 1)
			
			

		if self.addNode(node.leftChild, newNode) == True:
			return True

		else:
			if self.addNode(node.rightChild, newNode) == True:
				if node.right :
					self.topFreeLevel = self.topFreeLevel -1
					node.rightChild.right = True
				return True
		#self.topFreeLevel = self.topFreeLevel - 1
		#print('topFreeLevel now = ' + str(self.topFreeLevel))
		return False

	def traverse(self):
		self.topNode.traverse()
		
	def isFree(self, level):
		#return self.topNode.isFree(level)
		#return self.topNode.topFreeLevel()
		return self.topFreeLevel

