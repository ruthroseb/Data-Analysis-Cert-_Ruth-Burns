import requests
import pandas as pd

# import a CSV file into a Pandas DataFrame
data = pd.read_csv('Food_Production.csv')
print(data)
print(data.info())
print(data.describe())

# print first few rows , last few rows , missing values , sum of missing values
print(data.head())
print(data.tail())
print(data.isna().any())

# sorting
Total_Emissions_descending=data.sort_values("Total_emissions", ascending=False)
print(Total_Emissions_descending)
print(type(Total_Emissions_descending))

# Using Loc
# 1) food production data to all rows and columns 'food production' and 'total emissions'
# 2) food production data to first 6 rows and columns 'Food product','Packging' and 'Total_emissions'
# loc = selects data by columns and rows (names)
# animal_products = only rows that had animal feed > 0, processed_products = only rows that have processing emission >0
data_total_emissions=data.loc[:,['Food product', 'Total_emissions']]
Total_Emissions_descending=data_total_emissions.sort_values("Total_emissions", ascending=False)
animal_products=data.loc[data['Animal Feed']!=0]
print(animal_products)
processed_products=data.loc[data['Processing']!=0]
print(processed_products)


print(Total_Emissions_descending)
print(data.loc[:5,['Food product','Packging', 'Total_emissions']])

# Dropping duplicates - only checked for the name, because duplicate numbers should remain.
data_clean=data.drop_duplicates(subset="Food product")
data_clean["Food product"].value_counts(normalize=True)


