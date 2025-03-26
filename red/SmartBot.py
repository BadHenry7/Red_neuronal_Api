import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import RandomOverSampler  # Mejor que SMOTE para datos binarios
import joblib  

# Cargar el dataset
df = pd.read_csv("dataset2.csv", sep=";")

# **🔹 Eliminar espacios en los nombres de las columnas**
df.columns = df.columns.str.strip()

# Aplicar LabelEncoder a las enfermedades
label_encoder = LabelEncoder()
df['diseases'] = label_encoder.fit_transform(df['diseases'])

# Separar características (X) y etiquetas (y)
X = df.drop(columns=['diseases'])  # Todos los síntomas
y = df['diseases']  # La enfermedad en formato numérico

# Aplicar RandomOverSampler en lugar de SMOTE
oversampler = RandomOverSampler(random_state=42)
X_resampled, y_resampled = oversampler.fit_resample(X, y)

# **🔹 Asegurar que los nombres de las columnas de X están limpios**
X_resampled.columns = X_resampled.columns.str.strip()

# Verificar distribución después del balanceo
print("Distribución después de balanceo:\n", pd.Series(y_resampled).value_counts())

# División en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Entrenar el modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Evaluar el modelo
y_pred = modelo.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')
print(classification_report(y_test, y_pred))

# **🔹 Obtener la lista de síntomas disponibles (sin espacios extra)**
sintomas_disponibles = list(X.columns)

print("Lista de síntomas disponibles:", sintomas_disponibles)

# Entrada del usuario
entrada_usuario = input("Ingrese los síntomas separados por comas: ").strip().lower()
sintomas_usuario = [sintoma.strip() for sintoma in entrada_usuario.split(",")]

# **🔹 Convertir los síntomas ingresados en el mismo formato que los de X**
sintomas_validos = [s for s in sintomas_usuario if s in [x.lower() for x in sintomas_disponibles]]
print("✅ Síntomas reconocidos:", sintomas_validos)

# Crear array de entrada para el modelo
nuevos_sintomas = np.zeros((1, len(sintomas_disponibles)))
for sintoma in sintomas_validos:
    indice = [x.lower() for x in sintomas_disponibles].index(sintoma)
    nuevos_sintomas[0, indice] = 1

# **🔹 Crear DataFrame con las mismas columnas que el modelo**
nuevos_sintomas_df = pd.DataFrame(nuevos_sintomas, columns=sintomas_disponibles)

# **🔹 Asegurar que las columnas están en el mismo orden que en X**
nuevos_sintomas_df = nuevos_sintomas_df.reindex(columns=X.columns, fill_value=0)
print("🔍 Entrada al modelo:\n", nuevos_sintomas_df)

# Hacer la predicción
prediccion = modelo.predict(nuevos_sintomas_df)
enfermedad_predicha = label_encoder.inverse_transform(prediccion)

# Mostrar el resultado final
print(f'\n🩺 Enfermedad predicha: {enfermedad_predicha[0]}')

joblib.dump(modelo, 'smartbot_model.pkl')  
joblib.dump(label_encoder, 'smartbot_encoder.pkl')  
print("✅ SmartBot guardado exitosamente.") 