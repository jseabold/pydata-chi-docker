import pandas as pd
import requests

url = ("https://data.cityofchicago.org/api/views/4ijn-s7e5/rows.csv?"
       "accessType=DOWNLOAD")

response = requests.get(url, stream=True)

with open("Food_Inspections.csv", "wb") as fout:
    for chunk in response.iter_content(32 * 1024):
        fout.write(chunk)

df = pd.read_csv("Food_Inspection.csv")

for year, group in df.groupby(df['Inspection Date'].dt.year):
    group.to_csv("notebooks/data/food_inspection_{}.csv.gz".format(year),
                 compression='gzip', index=False)
