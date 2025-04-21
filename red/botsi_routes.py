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


# from fastapi import APIRouter, HTTPException
# import pandas as pd
# import numpy as np
# from pydantic import BaseModel
# import os
# import joblib

# router = APIRouter()

# import requests

# def descargar_archivo(url, nombre_destino):
#     if not os.path.exists(nombre_destino):
#         print(f"Descargando {nombre_destino}...")
#         respuesta = requests.get(url, stream=True)
#         with open(nombre_destino, 'wb') as archivo:
#             for chunk in respuesta.iter_content(chunk_size=8192):
#                 archivo.write(chunk)
#         print(f"{nombre_destino} descargado exitosamente.")
#     else:
#         print(f"{nombre_destino} ya existe. No se descarga.")

# # Reemplaza estos links con tus enlaces de descarga directa:
# modelo_url = "https://itsaedu-my.sharepoint.com/:u:/g/personal/hdavidromero_unibarranquilla_edu_co/EdP1tAv5S5xIsOpZkUwevHcBsBbXhjBMdeNe9-aPty8NkQ?e=TewQmf"
# encoder_url = "https://itsaedu-my.sharepoint.com/:u:/g/personal/hdavidromero_unibarranquilla_edu_co/EQC3hQSbUSVPimRXnUfjxRwBj0TareyGaU5Bio5zHnPYqQ?e=Vk3zqB"


# # Ruta donde deseas guardar
# ruta_modelo = "red/smartbot_model.pkl"
# ruta_encoder = "red/smartbot_encoder.pkl"

# # Llama la descarga antes de iniciar tu app
# descargar_archivo(modelo_url, ruta_modelo)
# descargar_archivo(encoder_url, ruta_encoder)

# # Cargar el dataset
# current_dir = os.path.dirname(__file__)  
# dataset_path = os.path.join(current_dir, "../red/dataset2.csv")  
# data = pd.read_csv(dataset_path, sep=";")

# # Cargar el modelo RandomForest y el LabelEncoder
# model_path = os.path.join(current_dir, "../red/smartbot_model.pkl")
# encoder_path = os.path.join(current_dir, "../red/smartbot_encoder.pkl")

# modelo = joblib.load(model_path)
# label_encoder = joblib.load(encoder_path)

# # Obtener lista de síntomas
# symptoms = data.drop(columns=["diseases"]).columns.tolist()

# # Modelo para recibir los síntomas seleccionados
# class PredictionRequest(BaseModel):
#     selected_symptoms: list[str]

# @router.get("/sintomas")
# async def get_symptoms():
#     return {"sintomas": symptoms}

# @router.post("/predict")
# async def predict_disease(request: PredictionRequest):
#     selected = request.selected_symptoms
    
#     # Crear vector binario de entrada
#     input_vector = [1 if symptom in selected else 0 for symptom in symptoms]
#     input_vector = np.array(input_vector).reshape(1, -1)
    
#     # Realizar predicción
#     pred = modelo.predict(input_vector)
#     enfermedad_predicha = label_encoder.inverse_transform(pred)[0]
    
#     return {"enfermedad": enfermedad_predicha}


from fastapi import APIRouter, HTTPException
import pandas as pd
import numpy as np
from pydantic import BaseModel
import os
import joblib
import gdown

router = APIRouter()

import requests

def descargar_archivo(url, nombre_destino):
    if os.path.exists(nombre_destino):
        print(f"{nombre_destino} ya existe. No se descarga.")
        return

    print(f"Descargando {nombre_destino}...")

    if "drive.google.com" in url:
        # Extraer ID del archivo
        if "id=" in url:
            file_id = url.split("id=")[-1]
        elif "/file/d/" in url:
            file_id = url.split("/file/d/")[1].split("/")[0]
        else:
            print("No se pudo extraer el ID de Google Drive.")
            return

        gdown_url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(gdown_url, nombre_destino, quiet=False)
    else:
        respuesta = requests.get(url, stream=True)
        if respuesta.status_code == 200:
            with open(nombre_destino, 'wb') as archivo:
                for chunk in respuesta.iter_content(chunk_size=8192):
                    archivo.write(chunk)
            print(f"{nombre_destino} descargado exitosamente.")
        else:
            print(f"Error al descargar {url}. Código de estado: {respuesta.status_code}")

# Reemplaza estos links con tus enlaces de descarga directa: 
modelo_url = "https://drive.google.com/uc?export=download&id=1ANtdNUEx5mlpYtNZFxvDfIgiTwHpyHSJ"
encoder_url = "https://drive.google.com/uc?export=download&id" \
"=1H-FOx_5swngKZV5tqduwi1_7aE_9_16m"

# model_path = os.path.join(current_dir, "../red/smartbot_model.pkl")
# encoder_path = os.path.join(current_dir, "../red/smartbot_encoder.pkl")
# Ruta donde deseas guardar
current_dir = os.path.dirname(__file__)  
ruta_modelo = os.path.join(current_dir, "../red/smartbot_model.pkl")
ruta_encoder =  os.path.join(current_dir, "../red/smartbot_encoder.pkl")

# Llama la descarga antes de iniciar tu app
descargar_archivo(modelo_url, ruta_modelo)
descargar_archivo(encoder_url, ruta_encoder)
