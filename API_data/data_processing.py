import json
import pandas as pd

with open('API_data\data.json', 'r') as f:
    data = json.load(f)


content = []
for letter in data:
    drink = letter['drinks']
    if drink:
        content.extend(drink)

df = pd.DataFrame(content)
print(df.head())
df.to_csv('API_data/drinks.csv')

