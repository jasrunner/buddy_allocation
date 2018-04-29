import sys


'''

A Node is created empty.  It keeps track of left and right children, which are themselves nodes.
The 'level' refers to the hierarchy.  The smaller the level, the smaller the size of the block this node represents.

'''

# set some parameters

maxBlock = 32
maxLevel = 5
minLevel = 1

# add Payload for data


class Node:

	# initialise to empty
	def __init__(self, level):

		self.level = level
		self.payload = ""
		self.leftChild = None
		self.rightChild = None

	# string representation for human readability
	def __str__(self):
		return "level={self.level}, payload={self.payload} ".format(self=self)

	# insert a child on the left
	def insertLeft(self, level):
		if level < minLevel:
			print('error in insertLeft, requested level is: ' + str(level))
			sys.exit()
		self.leftChild = Node(level)

	def insertRight(self, level):
		if level < minLevel:
			print('error in insertRight, requested level is: ' + str(level))
			sys.exit()
		self.rightChild = Node(level)

	def traverse(self):
		if self.isLeaf():
			print(self)
			
		if self.leftChild:
			self.leftChild.traverse()

		if self.rightChild:
			self.rightChild.traverse()

	def isAllocated(self):
		if self.payload == "":
			return False
		else:
			return True

	def isRightLevel(self, level):
		if self.level == level:
			return True

		else:
			return False

	def isLeaf(self):
		if self.leftChild is None:
			return True
		else:
			return False
			
	
	def isFree (self, level):
		if self.isRightLevel(level):
			
			if self.isLeaf() and not self.payload:
				return True
			else:
				return False
			
		if self.leftChild:
			if self.leftChild.isFree(level):
				return True

		if self.rightChild:
			if self.rightChild.isFree(level):
				return True
		
		return False
			
