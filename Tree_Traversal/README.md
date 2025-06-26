# Binary Search Tree (BST) in Python

This project implements a **Binary Search Tree** with standard operations such as `insert`, `search`, `delete`, and `in-order traversal`.

## Features

- Insert nodes into the BST
- Search for a specific value
- Delete a node while maintaining BST properties
- Traverse the tree in-order (returns sorted list)

## Class Structure

### `TreeNode`

Represents a single node in the tree.

```python
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
BinarySearchTree
Main class that manages the BST operations.

Methods:
insert(key): Inserts a new key into the tree.

search(key): Searches for a key and returns the corresponding node.

delete(key): Deletes the key from the tree.

inorder_traversal(): Returns a list of all keys in sorted (in-order) sequence.


bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

# Insert all nodes
for node in nodes:
    bst.insert(node)

# Search for a node
print('Search for 80:', bst.search(80))  # Should return TreeNode with key 80

# Inorder Traversal
print("Inorder traversal:", bst.inorder_traversal())  # Output: [20, 30, 40, 50, 60, 70, 80]

# Delete a node
bst.delete(40)

# Search after deletion
print("Search for 40:", bst.search(40))  # Should return None
print('Inorder traversal after deleting 40:', bst.inorder_traversal())  # Output: [20, 30, 50, 60, 70, 80]
```
Search for 80: 80
Inorder traversal: [20, 30, 40, 50, 60, 70, 80]
Search for 40: None
Inorder traversal after deleting 40: [20, 30, 50, 60, 70, 80]
License
This project is open-source and available under the MIT License.