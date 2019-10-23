# Key data structure in pandas is called a Data Frame
# DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.

#Ways of creating a Data Frame

#Dictionary
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)

# Reading from a csv file
# pldetails = pd.read_csv('~/code/python-intro/languagesandcreators.csv')
pldetails = pd.read_csv('~/code/python-intro/languagesandcreators.csv', index_col = 0)
print(pldetails)

# Accessing Columns
# Pandas Series
print(pldetails['Creators'])

# Pandas Dataframe
print(pldetails[['Year','Creators']])

# Accessing Rows
print(pldetails[0:2])

# iloc is index based
print(pldetails.iloc[2])

# loc is label based
print(pldetails.loc[['Python']])