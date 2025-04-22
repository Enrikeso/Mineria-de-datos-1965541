import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('clean_sugar_dataset.csv')

features = [
    'GDP_Per_Capita',
    'Avg_Retail_Price_Per_Kg',
    'Per_Capita_Sugar_Consumption',
    'Obesity_Rate',
    'Diabetes_Prevalence'
]

df_cluster = df[features].dropna()

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_cluster)

kmeans = KMeans(n_clusters=4, random_state=42)
df_cluster['Cluster'] = kmeans.fit_predict(scaled_data)

df['Cluster'] = -1
df.loc[df_cluster.index, 'Cluster'] = df_cluster['Cluster']

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_cluster, x='Per_Capita_Sugar_Consumption', y='Obesity_Rate', hue='Cluster', palette='Set2')
plt.title('Clustering de países por consumo de azúcar y obesidad')
plt.xlabel('Consumo de azúcar per cápita')
plt.ylabel('Tasa de obesidad')
plt.show()

print(df['Cluster'].value_counts())

'''
Este código agrupa los países usando K-Means, según su consumo de azúcar,
precio del azúcar, obesidad y diabetes. Usamos 4 grupos como ejemplo.
El gráfico ayuda a ver qué tan separados están los grupos en dos variables.
Esto sirve para entender patrones similares entre países.
'''