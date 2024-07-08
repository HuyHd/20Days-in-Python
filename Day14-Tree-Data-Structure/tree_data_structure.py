from collections import deque
from graphviz import Graph


class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def bfs(root):
    # If the tree is empty, return an empty list
    if root is None:
        return []

    result = []  # Initialize an empty list for the result
    queue = deque([root])  # Use deque to store nodes to be processed

    # Perform BFS traversal
    while queue:
        node = queue.popleft()  # Dequeue the first node
        # Append the value of the node to the result list
        result.append(node.val)

        # Enqueue left and right child nodes if they exist
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result  # Return the result list after traversal


def visualize_bfs_order(root, order):
    dot = Graph()  # Initialize a new Graphviz graph

    # Create node labels with traversal order information
    node_labels = {node.val: f"{node.val}" for node in order}
    for i, node in enumerate(order):
        node_labels[node.val] = f"{node.val} ({i+1})"

    # Recursive function to add edges and labels to the graph
    def add_edges_with_labels(dot, node):
        if node:
            # Add node with label
            dot.node(str(node.val), label=node_labels[node.val])
            if node.left:
                # Add edge to left child
                dot.edge(str(node.val), str(node.left.val))
                # Recursively add left subtree
                add_edges_with_labels(dot, node.left)
            if node.right:
                # Add edge to right child
                dot.edge(str(node.val), str(node.right.val))
                # Recursively add right subtree
                add_edges_with_labels(dot, node.right)

    # Start adding edges and labels from the root
    add_edges_with_labels(dot, root)
    return dot  # Return the Graphviz graph object


# Function to lookup nodes
def lookup(tree, key):
    if tree is None:
        return None  # If the tree is empty, return None

    q = deque([tree])  # Initialize a deque for level-order traversal

    # Perform level-order traversal
    while q:
        node = q.popleft()  # Get the next node

        if node.val == key:
            return node  # If the key is found, return the node

        if node.left:
            q.append(node.left)  # Add left child to the queue if it exists

        if node.right:
            q.append(node.right)  # Add right child to the queue if it exists

    return None  # If the key is not found, return None


# Function to insert nodes
def insert(root, data):
    # If tree is empty, new node becomes the root
    if root is None:
        root = Node(data)
        return root

    # Queue to traverse the tree and find the position to insert the node
    q = deque()
    q.append(root)
    while q:
        temp = q.popleft()
        # Insert node as the left child of the parent node
        if temp.left is None:
            temp.left = Node(data)
            break
        # If the left child is not null push it to the queue
        else:
            q.append(temp.left)
        # Insert node as the right child of parent node
        if temp.right is None:
            temp.right = Node(data)
            break
        # If the right child is not null push it to the queue
        else:
            q.append(temp.right)
    return root


# Function to delete the given deepest node (d_node) in binary tree
def delet_deepest(root, d_node):
    q = deque()
    q.append(root)

    # Do level order traversal until the last node
    while q:
        temp = q.popleft()

        # If the current node is the deepest node to be deleted
        if temp == d_node:
            temp = None  # Delete the node
            del d_node
            return

        # Check if the deepest node is in the right subtree
        if temp.right:
            if temp.right == d_node:
                temp.right = None  # Delete the node
                del d_node
                return
            else:
                q.append(temp.right)  # Continue traversal

        # Check if the deepest node is in the left subtree
        if temp.left:
            if temp.left == d_node:
                temp.left = None  # Delete the node
                del d_node
                return
            else:
                q.append(temp.left)  # Continue traversal


# Function to delete a node with a given key in binary tree
def deletion(root, key):
    if not root:
        return None

    # Case 1: Root is the only node in the tree
    if root.left is None and root.right is None:
        if root.data == key:
            return None  # Tree becomes empty
        else:
            return root  # Key not found, return the root as is

    q = deque()
    q.append(root)
    temp = None
    key_node = None

    # Do level order traversal to find the deepest node (temp) and node to be deleted (key_node)
    while q:
        temp = q.popleft()

        # Check if the current node matches the key
        if temp.val == key:
            key_node = temp

        # Enqueue the left child if exists
        if temp.left:
            q.append(temp.left)

        # Enqueue the right child if exists
        if temp.right:
            q.append(temp.right)

    # If the node to be deleted (key_node) is found
    if key_node is not None:
        x = temp.val  # Get the value of the deepest node
        key_node.val = x  # Replace the key_node's data with the deepest node's data
        delet_deepest(root, temp)  # Delete the deepest node
    return root  # Return the updated root of the tree


if __name__ == "__main__":
    root = None
    # Insertion of nodes
    values = [1, 2, 3, 4, 5]
    for value in values:
        root = insert(root, value)

    # Perform BFS
    bfs_result = bfs(root)
    print("BFS traversal result:", bfs_result)

    # Lookup node with key
    result = lookup(root, 4)
    if result:
        print(f"Node with key {result.val} found.")
    else:
        print("Key not found in the tree.")

    # Delete the node with data = 4
    root = deletion(root, 4)
    print("BFS after deletion:", bfs(root))
