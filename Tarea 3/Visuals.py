import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("clean_sugar_dataset.csv")

'''
df['Per_Capita_Sugar_Consumption'].plot(kind='hist', bins=20, edgecolor='black')
plt.title('Distribución del Consumo de Azúcar Per Cápita')
plt.xlabel('Kg de azúcar por persona/año')
plt.ylabel('Frecuencia')
plt.show()

sns.boxplot(data=df, x='Continent', y='Per_Capita_Sugar_Consumption')
plt.title('Consumo de Azúcar Per Cápita por Continente')
plt.xticks(rotation=45)
plt.show()

country = 'Mexico'
df_country = df[df['Country'] == country]
df_country.plot(x='Year', y='Total_Sugar_Consumption', marker='o')
plt.title(f'Consumo Total de Azúcar en {country} (año a año)')
plt.ylabel('Toneladas de azúcar')
plt.show()

plt.figure(figsize=(12,6))
sns.barplot(data=df, x='Region', y='Avg_Retail_Price_Per_Kg', estimator='mean')
plt.xticks(rotation=90)
plt.title('Precio Promedio del Azúcar por Región')
plt.show()
'''

df_europa = df[df['Continent'] == 'Europe']

plt.figure(figsize=(8,6))
sns.scatterplot(data=df_europa, x='Per_Capita_Sugar_Consumption', y='Diabetes_Prevalence', hue='Country', alpha=0.6)
plt.title('Europa: Consumo de Azúcar vs Prevalencia de Diabetes')
plt.show()