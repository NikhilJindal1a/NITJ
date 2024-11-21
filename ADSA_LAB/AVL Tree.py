# AVL Tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Function to get the height of the tree
def height(node):
    if not node:
        return 0
    return node.height

# Function to get the balance factor
def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

# Right rotate
def right_rotate(y):
    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x

# Left rotate
def left_rotate(x):
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

# Insert a node
def insert(node, key):
    # Perform normal BST insertion
    if not node:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # Update height of this ancestor node
    node.height = 1 + max(height(node.left), height(node.right))

    # Get the balance factor
    balance = get_balance(node)

    # Perform rotations to balance the tree
    # Left Left Case
    if balance > 1 and key < node.left.key:
        return right_rotate(node)

    # Right Right Case
    if balance < -1 and key > node.right.key:
        return left_rotate(node)

    # Left Right Case
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Right Left Case
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

# In-order traversal (to display the sorted elements)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

# Sample input
root = None
values = [10, 20, 30, 40, 50, 25]

# Build the AVL Tree
for value in values:
    root = insert(root, value)

print("In-order traversal of the AVL Tree:")
inorder_traversal(root)


# PS G:\Nikhil Jindal\Desktop\Mtech\Semester_1\ADSA_LAB> & C:/Users/Nikhil/AppData/Local/Programs/Python/Python312/python.exe "g:/Nikhil Jindal/Desktop/Mtech/Semester_1/ADSA_LAB/AVL Tree.py"
# In-order traversal of the AVL Tree:
# 10 20 25 30 40 50