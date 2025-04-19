import pandas as pd

from scipy.stats import f_oneway, kruskal

df = pd.read_csv("clean_sugar_dataset.csv")

# Agrupar la obesidad por continente
continent_groups = df.groupby("Continent")["Obesity_Rate"].apply(list)

anova_result = f_oneway(*continent_groups)
print("Resultado ANOVA:")
print("Estadístico F:", anova_result.statistic)
print("p-valor:", anova_result.pvalue)

kruskal_result = kruskal(*continent_groups)
print("\nResultado Kruskal-Wallis:")
print("Estadístico H:", kruskal_result.statistic)
print("p-valor:", kruskal_result.pvalue)

'''p-valor = 0.767 → Mucho mayor que 0.05
Conclusión: No hay evidencia estadística de que la obesidad promedio sea diferente entre continentes.'''