from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.rol_routes import router as Rol_router
from app.routes.atributo_routes import router as atributo_router
from app.routes.atributoxusuario_routes import router as atrixuser_router
from app.routes.cita_medica_routes import router as Cita_router
from app.routes.diagnosticos_routes import router as Diagnosticos_router
from app.routes.historial_routes import router as historial_router
from app.routes.sintomas_routes import router as sintomas_router
from red.botsi_routes import router as botci_router
from app.routes.token_routes import router as token_router
from app.routes.modulo_routes import router as modulo_router
from app.routes.moduloxperfil_routes import router as moduloxperfil_router
from app_Dynamobd.app import router as incapacidad_Dunamobd


from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
   allow_origins=[
         "http://localhost:5173",#Svelte
        "http://localhost:3000",#Node creo
        "http://localhost:4200",#Angular local
        "capacitor://localhost",#Para celulares
        "https://localhost",#Para celulares         
        "https://red-neuronal-api.onrender.com",#EL MISMO XD
        "https://api-nodejs-buxf.onrender.com",#Node
        "https://f882-191-110-53-32.ngrok-free.app",#ngrok
        "https://3f44-191-110-53-32.ngrok-free.app",#ngrok
        "https://red-neurolal-svelte.onrender.com",  # URL de Svelte
        "https://angular-red-neuronal.onrender.com" #URl de Angular

    ],
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(user_router) 
app.include_router(Rol_router)
app.include_router(atributo_router)  
app.include_router(atrixuser_router)  
app.include_router(Cita_router)  
app.include_router(Diagnosticos_router) 
app.include_router(historial_router) 
app.include_router(sintomas_router) 
app.include_router(botci_router)
app.include_router(token_router)
app.include_router(modulo_router)
app.include_router(moduloxperfil_router)
app.include_router(incapacidad_Dunamobd)




"""

@app.route('/')
def home():
    return ('+page.svelte')"""

"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 
"""
#...
#