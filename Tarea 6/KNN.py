import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("clean_sugar_dataset.csv")

features = [
    'GDP_Per_Capita', 'Urbanization_Rate', 'Processed_Food_Consumption',
    'Per_Capita_Sugar_Consumption', 'Avg_Daily_Sugar_Intake',
    'Obesity_Rate', 'Diabetes_Prevalence'
]
target = 'Continent'

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, df[target], test_size=0.3, random_state=42
)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("Reporte de clasificación:\n")
print(classification_report(y_test, y_pred))

print("Matriz de confusión:\n")
print(confusion_matrix(y_test, y_pred))


