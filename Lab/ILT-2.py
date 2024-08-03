# 1. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day).
import numpy as np
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
hot_days = temperatures > 35
cold_days = temperatures < 5
extreme_days = hot_days
extreme_temperatures = temperatures[extreme_days]
extreme_indices = np.where(extreme_days)[0]
cold_temperatures = temperatures[cold_days]
cold_indices = np.where(cold_days)[0]
print("Hot Days")
print("Days")
print(extreme_indices+1)
print("temperatures")
print(extreme_temperatures)
print("cold Days")
print("Days")
print(cold_indices+1)
print("temperatures")
print(cold_temperatures)
print("----------------------------------------------------------------------------------------------------------------")

# 2. split this data into quarterly reports for analysis and reporting purposes.
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
quarters = monthly_sales.reshape(4,3)
for i,quarter in enumerate(quarters,start=1):
    print(f"Quarter {i} sales:\n {quarter}")
print("----------------------------------------------------------------------------------------------------------------")
    
# 3. split this data into two groups: one group for customers who made a purchase in the last 30 days and another group for customers who haven't made a purchase in the last 30 days.
customer_ids = np.array([101,102,103,104,105,106,107,108,109,110])
last_purchase_days_ago = np.array([5,15,20,25,30,35,40,45,50,55])
recent_customers = customer_ids[last_purchase_days_ago <= 30]
inactive_customers = customer_ids[last_purchase_days_ago > 30]
print("Active customers ( last purchase <= 30 days ago):\n", recent_customers)
print("Inactive customers ( last purchase > 30 days ago):\n", inactive_customers)
print("----------------------------------------------------------------------------------------------------------------")

# 4. combine this data to create a comprehensive employee dataset for HR analysis.
full_time_employees = np.array([
[101, 'John Doe', 'Full-Time', 55000],
[102, 'Jane Smith', 'Full-Time', 60000],
[103, 'Mike Johnson', 'Full-Time', 52000]
])
part_time_employees = np.array([
[201, 'Alice Brown', 'Part-Time', 25000],
[202, 'Bob Wilson', 'Part-Time', 28000],
[203, 'Emily Davis', 'Part-Time', 22000]
])
