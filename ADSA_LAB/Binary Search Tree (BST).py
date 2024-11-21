# Binary Search Tree (BST)

# Define the node structure
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insert a node into the BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Search for a value in the BST
def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

# In-order traversal (optional, to display sorted elements)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

# Sample input
root = None
values = [50, 30, 70, 20, 40, 60, 80]

# Build the BST
for value in values:
    root = insert(root, value)

print("In-order traversal of the BST:")
inorder_traversal(root)

# Search for a key
key_to_search = 40
result = search(root, key_to_search)
if result:
    print(f"\nElement {key_to_search} found in the BST.")
else:
    print(f"\nElement {key_to_search} not found in the BST.")
