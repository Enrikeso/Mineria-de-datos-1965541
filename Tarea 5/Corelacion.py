import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("clean_sugar_dataset.csv")

X = df[["Per_Capita_Sugar_Consumption", "Obesity_Rate", "GDP_Per_Capita", "Avg_Daily_Sugar_Intake"]]
y = df["Diabetes_Prevalence"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

r2 = r2_score(y_test, y_pred)
print("R² score del modelo:", r2)

plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel("Valores reales")
plt.ylabel("Predicciones")
plt.title("Modelo Lineal: Valores Reales vs Predichos")
plt.grid(True)
plt.show()

'''El R² obtenido fue bajo, lo cual indica que el modelo no logra explicar 
bien la variabilidad de los datos. Esto tiene sentido, ya que en la Tarea 4 
se comprobó que la obesidad no varía significativamente entre continentes 
(p > 0.05), lo que sugiere que estas variables no tienen un poder predictivo 
fuerte en este caso.'''