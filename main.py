import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# import a CSV file into a Pandas DataFrame
data = pd.read_csv('Food_Production.csv')
print(data)
print(data.info())
print(data.describe())

# print first few rows , last few rows , missing values , sum of missing values
print(data.head())
print(data.tail())
print(data.isna().any())

# Dropping duplicates - only checked for the name, because duplicate numbers should remain.
data_clean=data.drop_duplicates(subset="Food product")
data_clean["Food product"].value_counts(normalize=True)

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
animal_products_descending=animal_products.sort_values("Total_emissions",ascending=False)
print(animal_products)
animal_products_mean=animal_products['Total_emissions'].mean()

#processed products
processed_products=data.loc[data['Processing']!=0]
print(processed_products)
nonprocessed_products=data.loc[data['Processing']==0]
print(nonprocessed_products)
process_Products_mean=processed_products['Total_emissions'].mean()
nonprocessed_products_mean=nonprocessed_products['Total_emissions'].mean()
print(process_Products_mean)

print(Total_Emissions_descending)
print(data.loc[:5,['Food product','Packging', 'Total_emissions']])

for lab, row in data.iterrows():
    print(lab)
    print(row)

#oil products
oils=data.loc[[15,16,17,18,19],]
oils_desc=oils.sort_values('Total_emissions',ascending=False)
print(oils_desc)
oils_mean=oils['Total_emissions'].mean()

#fruits
fruits=data.loc[[27,25,30,26,28],]
fruits_mean=fruits['Total_emissions'].mean()

#vegetables
vegetables=data.loc[[21,5,22,24,10,],]
vegetables_mean=vegetables['Total_emissions'].mean()

fig, ax = plt.subplots()
plt.xticks(rotation=45)
ax.plot(oils_desc['Food product'],oils_desc['Total_emissions'],marker='o',linestyle='None', color='y')
ax.bar(oils_desc['Food product'], oils_desc['Land use change'],label='Land use change')
ax.bar(oils_desc['Food product'], oils_desc['Farm'],bottom=oils_desc['Land use change'], label='Farm')
ax.bar(oils_desc['Food product'], oils_desc['Processing'],bottom=oils_desc['Land use change']+oils_desc['Farm'],label='Processing')
ax.bar(oils_desc['Food product'], oils_desc['Packging'],bottom=oils_desc['Land use change']+oils_desc['Farm']+oils_desc['Processing'],label='Packging')
ax.bar(oils_desc['Food product'], oils_desc['Transport'],bottom=oils_desc['Land use change']+oils_desc['Farm']+oils_desc['Processing']+oils_desc['Packging'],label='Transport')
ax.set_title('Total emissions and impacting variables by oil type')
plt.ylabel("Greenhouse emissions (kg CO2 - equivalents per kg product)")
plt.legend()

fig, ax = plt.subplots()
plt.xticks(rotation=45)
ax.bar(animal_products_descending['Food product'], animal_products_descending['Animal Feed'],label="Animal Feed")
ax.bar(animal_products_descending['Food product'], animal_products_descending['Land use change'],label='Land use change')
ax.bar(animal_products_descending['Food product'], animal_products_descending['Animal Feed'],label='Animal Feed')
ax.bar(animal_products_descending['Food product'], animal_products_descending['Farm'],label='Farm')
ax.bar(animal_products_descending['Food product'], animal_products_descending['Processing'],label='Processing')
ax.bar(animal_products_descending['Food product'], animal_products_descending['Transport'],label='Transport')
ax.bar(animal_products_descending['Food product'], animal_products_descending['Packging'],label='Packging')
ax.bar(animal_products_descending['Food product'], animal_products_descending['Retail'],label='Retail')
ax.set_title('Animal Food Product Environmental impact by variables')
plt.ylabel("Greenhouse emissions (kg CO2 - equivalents per kg product)")
plt.xlabel("Food Category")

plt.legend()


fig, ax = plt.subplots()
plt.xticks(rotation=45)
x=("Animal Products", "Oil Products", "Processed Products", "Non Processed Products", "Fruits", "Vegetables")
y = (animal_products_mean, oils_mean, process_Products_mean, nonprocessed_products_mean, fruits_mean,vegetables_mean)
ax.plot(x,y,marker='X',linestyle='None', color='r')
ax.set_title('Total emissions by food category')
plt.ylabel("Greenhouse emissions (kg CO2 - equivalents per kg product)")
plt.xlabel("Food Category")



fig, ax = plt.subplots()
plt.xticks(rotation=45)
ax.bar(animal_products_descending['Food product'], animal_products_descending['Eutrophying emissions per 1000kcal (gPO₄eq per 1000kcal)'], label="Eutrophying emissions")
ax.bar(animal_products_descending['Food product'], animal_products_descending['Freshwater withdrawals per 1000kcal (liters per 1000kcal)'],bottom=animal_products_descending['Eutrophying emissions per 1000kcal (gPO₄eq per 1000kcal)'],label='Freshwater withdrawals')
ax.bar(animal_products_descending['Food product'], animal_products_descending['Greenhouse gas emissions per 1000kcal (kgCO₂eq per 1000kcal)'],bottom=animal_products_descending['Freshwater withdrawals per 1000kcal (liters per 1000kcal)'],label='Greenhouse gas emissions')
ax.bar(animal_products_descending['Food product'], animal_products_descending['Land use per 1000kcal (m² per 1000kcal)'],bottom=animal_products_descending['Greenhouse gas emissions per 1000kcal (kgCO₂eq per 1000kcal)'],label='Land use')
ax.set_title('Animal Food Product Environmental impact by variables (per 1000kcal)')
plt.legend()

#find food with low emissions
low_emmissions_product=data.loc[data['Total_emissions']<2]
print(low_emmissions_product)

#comparing emission product weight to calories
fig, ax = plt.subplots()
plt.xticks(rotation=45)
ax.plot(animal_products_descending['Food product'],animal_products_descending['Total_emissions'], label="Emissions per kg of product", marker='o' )
ax.plot(animal_products_descending['Food product'],animal_products_descending['Greenhouse gas emissions per 1000kcal (kgCO₂eq per 1000kcal)'], label="Emissions per 1000kcal", marker='o')
ax.plot(animal_products_descending['Food product'],animal_products_descending['Greenhouse gas emissions per 100g protein (kgCO₂eq per 100g protein)'], label="Emissions per 100g protein", marker='o')
ax.set_title('Animal Food ProductTotal Emissions: /kg of product v /kg 1000kcal v /100g protein')
plt.legend()


fig, ax = plt.subplots()
sns.scatterplot(data=low_emmissions_product, x="Total_emissions", y="Scarcity-weighted water use per kilogram (liters per kilogram)")
plt.text(0.2, 220000, "Nuts")
ax.set_title('Low emission food products by scarcity water use')

plt.legend()


plt.show()