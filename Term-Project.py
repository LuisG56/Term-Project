import random
import time

# So this will be Part 1: The data structure
class CarNode:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.left = None
        self.right = None
        self.substree_sum = price # This is the memoization: This stores the sum of this node and all children

class CarInventoryBST:
    def __init__(self):
        self.root = None

    def insert(self, model, price):
        if self.root is None:
            self.root = CarNode(model, price)
        else:
            self.insert_recursive(self.root, model, price):
        