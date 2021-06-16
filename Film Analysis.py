
# API (omdb api key is 87c8a7a3)
r_harrypotter=requests.get('http://www.omdbapi.com/?apikey=87c8a7a3&t=harry+potter&plot=full')
r_lordoftherings=requests.get('http://www.omdbapi.com/?apikey=87c8a7a3&t=lord+of+the+rings&plot=full')
print(r_harrypotter.text)
print(r_lordoftherings.text)
