import binaryTree

def sum(a,b):
    sum = a+b
    return sum

a=1
b=2
c=sum(a,b)
print(c)

testNode = binaryTree.Node(5)
binaryTree.insert(testNode, 2)
binaryTree.inorder(testNode)
