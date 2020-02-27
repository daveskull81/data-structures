import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        def recurse_insert(node, newValue):
            if node is None:
                node = BinarySearchTree(newValue)
                return
            elif newValue < node.value:
                if node.left is None:
                    node.left = BinarySearchTree(newValue)
                else:
                    recurse_insert(node.left, newValue)
            else:
                if node.right is None:
                    node.right = BinarySearchTree(newValue)
                else:
                    recurse_insert(node.right, newValue)

        recurse_insert(self, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        def recurse_contains(node, targetValue):
            if node is None:
                return False
            if node.value == targetValue:
                return True
            if targetValue < node.value:
                return recurse_contains(node.left, targetValue)
            else:
                return recurse_contains(node.right, targetValue)

        return recurse_contains(self, target)

    # Return the maximum value found in the tree
    def get_max(self):
        
        def recurse_max(node):
            if node.right is None:
                return node.value
            else:
                return recurse_max(node.right)

        return recurse_max(self)

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        
        def recurse_for_each(node, func_to_call):

            if node is not None:
                func_to_call(node.value)
                recurse_for_each(node.left, func_to_call)
                recurse_for_each(node.right, func_to_call)
            else:
                return

        recurse_for_each(self, cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)

        while queue.len() > 0:
            temp = queue.dequeue()
            print(temp.value)
            if temp.right:
                queue.enqueue(temp.right)
            if temp.left:
                queue.enqueue(temp.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)

        while stack.len() > 0:
            temp = stack.pop()
            print(temp.value)
            if temp.right:
                stack.push(temp.right)
            if temp.left:
                stack.push(temp.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass