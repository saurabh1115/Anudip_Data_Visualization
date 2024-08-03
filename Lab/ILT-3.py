import numpy as np

# 1. find the total revenue
revenue1 = np.array([500,600,700,550])
revenue2 = np.array([450,700,800,600])
total = revenue1+revenue2
print("Total Revenue = ",total)

# 2. calculate the profit made by the company
revenue = np.array([10000,12000,11000,10500])
expenses = np.array([4000,8000,4500,4800])
profit = revenue-expenses
print("Profit = ",profit)

# 3. determine which products are out of stock
inventory = np.array([10,0,5,0,20,0])
print("out of stock = ",inventory[inventory==0])
        
# 4. Calculate the total cost of items in a shopping cart
quantity = np.array([2, 3, 4, 1])
price_per_item = np.array([10.0,5.0,8.0,12.0])
total_cost = quantity*price_per_item
print("Total cost = ",total_cost)