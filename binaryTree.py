
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def insert(node, key):
    if node == None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def minValueSucessor(node):
    if node.left == None:
        return node
    if node.left != None:
        return minValueSucessor(node.left)


def delete(node, key):
    if node == None:
        return node
    
    #if less, go left
    if key < node.key:
        node.left = delete(node.left, key)
    #elif greater, go right
    elif key > node.key:
        node.right = delete(node.right, key)
    #elif found:
    elif key == node.key:
        # 0-1 child handling
        if node.left == None:
            temp = node.right
            node = None
            return temp
        elif node.right == None:
            temp = node.left
            node = None
            return temp
        # 2 child handling - this code will run if the other if statements dont trigger
        temp = minValueSucessor(node.right)
        node.key = temp.key
        node.right=delete(node.right, temp.key)


    return node



#Driver code
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = delete(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)