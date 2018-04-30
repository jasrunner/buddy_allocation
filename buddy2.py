import sys
import node
import tree


'''
Using a binary tree in a buddy-system style allocation technique
to optimally allocate space
'''

# <TODO>: add tree - get tree to keep track of how many 'Free' nodes there are


def findLevel(u, size):
	if 2**(u - 1) < size <= 2**u:
		#if the size is between the two levels, return this level
		return u
	else:

		# if the lower limit is reached, return this level
		if u == node.minLevel:
			return u
		# recursively descend levels
		return findLevel(u - 1, size)



u = node.maxLevel
size = 4

if size > node.maxBlock:
	print('size is too big')
	sys.exit()

level = findLevel(u, size)

n1 = node.Node(3)
n1.payload = 'Ben'

n2 = node.Node(3)
n2.payload = 'Jen'

n3 = node.Node(2)
n3.payload = 'Finn'

n4 = node.Node(2)
n4.payload = 'El'

n5 = node.Node(1)
n5.payload = 'Loki'

n6 = node.Node(level)
n6.payload = 'Bergen'

# start a tree
tree = tree.Tree(node.maxLevel)

#print(tree)
print ('top free level = ' + str(tree.isFree(level))) 
print("Adding n3")

if not tree.addNode(tree.topNode, n3):
	print("exiting")
	tree.traverse()
	sys.exit()

print ('top free level = ' + str(tree.isFree(level))) 
print("Adding n4")

if not tree.addNode(tree.topNode, n4):
	print("exiting")
	tree.traverse()
	sys.exit()

print ('top free level = ' + str(tree.isFree(level))) 
print("Adding n2")

if not tree.addNode(tree.topNode, n2):
	print("exiting")
	tree.traverse()
	sys.exit()

print ('top free level = ' + str(tree.isFree(level))) 
print("Adding n1")

if not tree.addNode(tree.topNode, n1):
	print("exiting")
	tree.traverse()
	sys.exit()

print ('top free level = ' + str(tree.isFree(level))) 
print("Adding n5")

if not tree.addNode(tree.topNode, n5):
	print("exiting")
	sys.exit()


print ('top free level = ' + str(tree.isFree(level))) 	
print("Adding n6")

if not tree.addNode(tree.topNode, n6):
	print("exiting")
	sys.exit()
	
tree.traverse()

print ('top free level = ' + str(tree.isFree(level))) 	
#else :
	#print ('no space for level ' + str(level))

