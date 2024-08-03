import pandas as pd

# series display
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
'October', 'November', 'December']
sales_data = [12000, 13500, 14200, 12800, 14000, 15500, 16200, 15800, 16500,
17800, 18500, 17200]
sales_series = pd.Series(sales_data, index=months, name='Monthly Sales (USD)')
print(sales_series)

# creating dataframe
data = {'Name': ['mia', 'emily', 'raley', 'sunny'],'Age': [25, 30, 35, 28]}
df = pd.DataFrame(data)
print("Initial\n",df)

# adding new column
df['States'] = ['delhi', 'UP', 'kashmir', 'goa']
print("new column\n",df)

# adding multiple columns
new_columns = {
'Gender': ['Female', 'Female', 'Female', 'Female'],
'Grade': ['A', 'B', 'C', 'B']
}
df['Gender'] = new_columns['Gender']
df['Grade'] = new_columns['Grade']
print("multiple column\n",df)

# adding new row
new_row = pd.DataFrame([{'Name':'eva','Age':'22','States':'delhi','Gender':'Female','Grade':'A'}])
df = pd.concat([df,new_row],ignore_index=True)
print("new row\n",df)

# adding new row at specific index
new_row = {'Name':'v','Age':'20','States':'JK','Gender':'Female','Grade':'A'}
index = 2
df.loc[index] = new_row
df = df.sort_index().reset_index(drop=True)
print("raw at specific index\n",df)

# adding multiple rows
new_rows = pd.DataFrame([
{'Name': 'a', 'Age': 98, 'States': 'goa','Gender':'Male','Grade':'A'},
{'Name': 'b', 'Age': 99, 'States': 'MP','Gender':'Male','Grade':'A'},
{'Name': 'c', 'Age': 100, 'States': 'UP','Gender':'Male','Grade':'A'}
])
df = pd.concat([df, new_rows], ignore_index=True)
print("multiple rows\n",df)

# Updating Value
fruit_data = {"Fruit": ['Apple','Avacado','Banana','Strawberry','Grape'],"Colour":
['Red','Green','Yellow','Pink','Green'],
"Price": [45, 90, 60, 37, 49]
}
data = pd.DataFrame(fruit_data)
print("Before\n")
print(data)
data=data.rename(columns = {'Fruit':'Fruit Name','Colour':'Color','Price':'Cost'})
print("After\n")
print(data)
print("Display 4th row Value")
print(data.loc[3])
print("After updating values")
print(data)
print(data.loc[3,['Fruit Name']])

# 
fruit_data = {"Fruit": ['Apple','Avacado','Banana','Strawberry','Grape'],"Colour":
['Red','Green','Yellow','Pink','Green'],
"Cost": [45, 90, 60, 37, 49]
}
data = pd.DataFrame(fruit_data)
data.loc[data['Cost']>=60,'Remarks'] = 'mehenga'
data.loc[data['Cost']<60,'Remarks'] = 'sasta'
print(data)