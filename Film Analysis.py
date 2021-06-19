import requests
import pandas as pd
import numpy as np
import matplotlib

# API (omdb api key is 87c8a7a3)
r_harrypotter=requests.get('http://www.omdbapi.com/?apikey=87c8a7a3&t=harry+potter&plot=full')
r_lordoftherings=requests.get('http://www.omdbapi.com/?apikey=87c8a7a3&t=lord+of+the+rings&plot=full')
print(type(r_harrypotter))

print(r_harrypotter.text)
print(r_lordoftherings.text)
# print as a dictionary
print(r_harrypotter.json())
print(r_lordoftherings.json())

# rating
print(r_harrypotter.json()["Ratings"])

# looping a dictionary
x=r_harrypotter.json()
y=r_lordoftherings.json()
for key, value in x.items():
    print(key + ": " + str(value))

df_harrypotter = pd.DataFrame.from_dict(x, orient='index')
df_lordoftherings = pd.DataFrame.from_dict(y, orient='index')

concat_data=pd.concat([df_harrypotter,df_lordoftherings], axis=1)
print(concat_data)
