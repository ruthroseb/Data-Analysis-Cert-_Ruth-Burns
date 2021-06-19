import pandas as pd
import matplotlib.pyplot as plt

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
animal_products_descending=animal_products.sort_values("Total_emissions", ascending=False)
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
ax.bar(oils_desc['Food product'], oils_desc['Farm'],label='Farm')
ax.bar(oils_desc['Food product'], oils_desc['Processing'],label='Processing')
ax.bar(oils_desc['Food product'], oils_desc['Packging'],label='Packging')
ax.set_title('Total Emissions and impacting variables by Oil Type')
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
plt.legend()


fig, ax = plt.subplots()
plt.xticks(rotation=45)
x=("Animal Products", "Oil Products", "Processed Products", "Non Processed Products", "Fruits", "Vegetables")
y = (animal_products_mean, oils_mean, process_Products_mean, nonprocessed_products_mean, fruits_mean,vegetables_mean)
ax.plot(x,y,marker='o',linestyle='None', color='y')


fig, ax = plt.subplots()
plt.xticks(rotation=45)
ax.bar(animal_products_descending['Food product'], animal_products_descending['Eutrophying emissions per 1000kcal (gPO₄eq per 1000kcal)'], label="Eutrophying emissions")
ax.bar(animal_products_descending['Food product'], animal_products_descending['Freshwater withdrawals per 1000kcal (liters per 1000kcal)'],bottom=animal_products_descending['Eutrophying emissions per 1000kcal (gPO₄eq per 1000kcal)'],label='Freshwater withdrawals')
ax.bar(animal_products_descending['Food product'], animal_products_descending['Greenhouse gas emissions per 1000kcal (kgCO₂eq per 1000kcal)'],bottom=animal_products_descending['Freshwater withdrawals per 1000kcal (liters per 1000kcal)'],label='Greenhouse gas emissions')
ax.bar(animal_products_descending['Food product'], animal_products_descending['Land use per 1000kcal (m² per 1000kcal)'],bottom=animal_products_descending['Greenhouse gas emissions per 1000kcal (kgCO₂eq per 1000kcal)'],label='Land use')
ax.set_title('Animal Food Product Environmental impact by variables (per 1000kcal)')
plt.legend()

plt.show()
