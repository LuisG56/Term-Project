import random
import time

# So this will be Part 1: The data structure
class CarNode:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.left = None
        self.right = None
        self.subtree_sum = price # This is the memoization: This stores the sum of this node and all children

class CarInventoryBST:
    def __init__(self):
        self.root = None

    def insert(self, model, price):
        if self.root is None:
            self.root = CarNode(model, price)
        else:
            self.insert_recursive(self.root, model, price)

    def insert_recursive(self, current, model, price):
        current.subtree_sum += price # Bookeeping: It updates the memoized sum on the way down

        if price < current.price:
            if current.left is None:
                current.left = CarNode(model, price)
            else:
                self.insert_recursive(current.left, model, price)
        else:
            if current.right is None:
                current.right = CarNode(model, price)
            else:
                self.insert_recursive(current.right, model, price)

    def get_range_value(self, low, high):
        return self.range_recursive(self.root, low, high)

    def range_recursive(self, node, low, high):
        if node is None:
            return 0
    # If node is in range, add the price and search both sides 
        if low <= node.price <= high:
            return node.price + self.range_recursive(node.left, low, high) + self.range_recursive(node.right, low, high)
        # If the node is too expensive, only search the left
        elif node.price > high:
            return self.range_recursive(node.left, low, high)
        # If node is cheap, search the right only
        else:
            return self.range_recursive(node.right, low, high)

# Part 2: Making fake cars
def make_fake_car_data(count):
    brand = ["Ford", "Chevy", "Telsa", "Dodge", "BMW"]
    models = ["Sedan", "SUV", "Truck"]
    data = []
    for _ in range(count):
        data.append({"name": f"{random.choice(brand)} {random.choice(models)}", "price": random.randint(15000, 85000)})
    return data     

# Part 3: The demo and testing the time
num_cars = 100000 # We can change the number to 1000 or 10000 etc.
test_data = make_fake_car_data(num_cars)
inventory = CarInventoryBST()

# Populate the tree
for car in test_data:
    inventory.insert(car["name"], car["price"])

print(f"---Performance Test: {num_cars:,} Cars---")

# Test the BST (memorized)
start_bst = time.perf_counter()
total_val_bst = inventory.root.subtree_sum
end_bst = time.perf_counter()

# Test the list
price_list = [c["price"] for c in test_data]
start_list = time.perf_counter()
total_val_list = sum(price_list) 
end_list = time.perf_counter()

# results
print(f"Standard List Time: {end_list - start_list:.10f} seconds")
print(f"Memoized BST Time: {end_bst - start_bst:.10f} second")
print(f"BST is roughly {int((end_list - start_list)/(end_bst - start_bst))}x faster!")
print(f"Final Inventory Value: ${total_val_bst:,.2f}")