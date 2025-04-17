import pandas as pd

df = pd.read_csv("clean_sugar_dataset.csv")

print(df.describe())
print(df.columns)

#ENTIDAD: País
print("Estadísticas por País:")
print(df.groupby("Country")[["GDP_Per_Capita", "Urbanization_Rate", "Population"]].mean())

#ENTIDAD: Comercio
print("\nComercio (Importaciones, Exportaciones y Precio Promedio por país):")
print(df.groupby("Country")[["Sugar_Imports", "Sugar_Exports", "Avg_Retail_Price_Per_Kg"]].mean())

#ENTIDAD: Políticas
print("\nPolíticas gubernamentales promedio por país:")
print(df.groupby("Country")[["Gov_Tax", "Gov_Subsidies"]].mean())

#ENTIDAD: Producción de Azúcar
print("\nProducción de azúcar agrupada por país:")
print(df.groupby("Country")[["Sugar_From_Sugarcane", "Sugar_From_Beet", "Sugar_From_HFCS", "Sugar_From_Other", "Sugarcane_Production_Yield"]].mean())

#ENTIDAD: Consumo de Azúcar
print("\nConsumo de azúcar por país:")
print(df.groupby("Country")[["Per_Capita_Sugar_Consumption", "Total_Sugar_Consumption", "Avg_Daily_Sugar_Intake", "Processed_Food_Consumption"]].mean())

#ENTIDAD: Factores Ambientales
print("\nFactores Ambientales promedio por país:")
print(df.groupby("Country")[["Urbanization_Rate", "Climate_Conditions"]].mean())

#ENTIDAD: Población
print("\nEstadísticas de población por país:")
print(df.groupby("Country")[["Population", "GDP_Per_Capita"]].mean())

#ENTIDAD: Diabetes
print("\nDiabetes y obesidad promedio por país:")
print(df.groupby("Country")[["Obesity_Rate", "Diabetes_Prevalence"]].mean())