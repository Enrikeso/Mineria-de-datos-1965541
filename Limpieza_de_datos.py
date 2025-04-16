import pandas as pd

df = pd.read_csv("sugar_consumption_dataset.csv")


print(df.head())

print(df.info())

print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

print(df.isnull().sum())

print(df[['Gov_Tax', 'Education_Campaign']].head(10))

gov_tax_mean = df['Gov_Tax'].mean()
education_campaign_mean = df['Education_Campaign'].mean()

print(f"Promedio Gov_Tax: {gov_tax_mean}")
print(f"Promedio Education_Campaign: {education_campaign_mean}")

df['Gov_Tax'] = df['Gov_Tax'].fillna(0)
df['Education_Campaign'] = df['Education_Campaign'].fillna(0)

print(df.isnull().sum())

df['Year'] = pd.to_datetime(df['Year'], format='%Y')

df.to_csv("clean_sugar_dataset.csv", index=False)
