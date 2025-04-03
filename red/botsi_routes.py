from fastapi import APIRouter, HTTPException
import pandas as pd
import numpy as np
from pydantic import BaseModel
import os
import joblib

router = APIRouter()

# Cargar el dataset
current_dir = os.path.dirname(__file__)  
dataset_path = os.path.join(current_dir, "../red/dataset2.csv")  
data = pd.read_csv(dataset_path, sep=";")

# Cargar el modelo RandomForest y el LabelEncoder
model_path = os.path.join(current_dir, "../red/smartbot_model.pkl")
encoder_path = os.path.join(current_dir, "../red/smartbot_encoder.pkl")

modelo = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)

# Obtener lista de síntomas
symptoms = data.drop(columns=["diseases"]).columns.tolist()

# Modelo para recibir los síntomas seleccionados
class PredictionRequest(BaseModel):
    selected_symptoms: list[str]

@router.get("/sintomas")
async def get_symptoms():
    return {"sintomas": symptoms}

@router.post("/predict")
async def predict_disease(request: PredictionRequest):
    selected = request.selected_symptoms
    
    # Crear vector binario de entrada
    input_vector = [1 if symptom in selected else 0 for symptom in symptoms]
    input_vector = np.array(input_vector).reshape(1, -1)
    
    # Realizar predicción
    # pred = modelo.predict(input_vector)
    # enfermedad_predicha = label_encoder.inverse_transform(pred)[0]
    
     # Realizar predicción con probabilidad
    probabilities = modelo.predict_proba(input_vector)
    
    # Obtener el índice de la enfermedad con mayor probabilidad
    indice_predicho = np.argmax(probabilities)
    enfermedad_predicha = label_encoder.inverse_transform([indice_predicho])[0]
    probabilidad_predicha = probabilities[0, indice_predicho] * 100  # Convertir a porcentaje

    return {
        "enfermedad": enfermedad_predicha,
        "probabilidad": f"{probabilidad_predicha:.2f}%"
    }





























# from fastapi import FastAPI
# from fastapi import APIRouter, HTTPException
# import pandas as pd
# import numpy as np
# from pydantic import BaseModel
# from tensorflow.keras.models import load_model
# import os

# router = APIRouter()
# # Cargar el dataset y el modelo
# #data = pd.read_csv("../red/dataset2.csv", sep=";")

# current_dir = os.path.dirname(__file__)  # Directorio del script actual
# dataset_path = os.path.join(current_dir, "../red/dataset2.csv")  # Ajusta si es necesario
# data = pd.read_csv(dataset_path, sep=";")



# #model = load_model("../red/botci.h5")

# current_dir = os.path.dirname(__file__)  # Directorio actual del script
# model_path = os.path.join(current_dir, "../red/botci.h5")
# model = load_model(model_path)

# # Obtener lista de síntomas y enfermedades
# symptoms = data.drop(columns=["diseases"]).columns.tolist()
# diseases = data["diseases"].unique().tolist()



# # Modelo para recibir los síntomas seleccionados
# class PredictionRequest(BaseModel):
#     selected_symptoms: list[str]

# @router.get("/sintomas")
# async def get_symptoms():
   

#     return {"sintomas": symptoms}

# @router.post("/predict")
# async def predict_disease(request: PredictionRequest):
#     # Crear un vector de entrada con los síntomas seleccionados
#     selected = request.selected_symptoms
#     input_vector = [1 if symptom in selected else 0 for symptom in symptoms]
#     input_vector = np.array(input_vector).reshape(1, -1)

#     # Hacer la predicción
#     result = model.predict(input_vector)
#     predicted_class = np.argmax(result)
#     predicted_disease = diseases[predicted_class]

#     return {"enfermedad": predicted_disease}
