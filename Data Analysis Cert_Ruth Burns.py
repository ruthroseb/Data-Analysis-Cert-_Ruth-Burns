import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# import a CSV file into a Pandas DataFrame
data = pd.read_csv('Food_Production.csv')

Total_Emissions_descending=data.sort_values("Total_emissions", ascending=False)
print(Total_Emissions_descending)