import boto3
from fastapi import FastAPI
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date
from datetime import datetime
import time
import os
# Especifica las credenciales y la region

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION')



#crea un cliente de Dynamodb
dynamodb= boto3.client('dynamodb',
              region_name= aws_region,
              aws_access_key_id= aws_access_key_id,
              aws_secret_access_key= aws_secret_access_key)#




#Nombre de la tabla en DynamoDB
nombre_tabla='Incapacidades'
#Realiza la operacion de lectura (scan) en la tabla

response= dynamodb.scan(TableName=nombre_tabla)
#Itera sobre los elementos obtenidos e imprime sus valores

#print ("---------------------------------------------------------------------",response)





router = APIRouter()


class Incapacidad(BaseModel):
    descripcion: str
    dias_de_incapacidad: str
    id_usuario: int
    id_doctor: int
    observaciones: str

class Buscar(BaseModel):
    id_usuario: int


@router.post('/incapacidad_medica')
async def get_incapacidad(user: Buscar):
    print ("-----------------------",user)
    response = dynamodb.scan(
    TableName=nombre_tabla,
    FilterExpression='id_usuario = :id',
    ExpressionAttributeValues={
        ':id': {'N': str(user.id_usuario)}
    }
    )
    for item in response['Items']:
        identificacion = item['identificacion']['N']
        descripcion= item['descripcion']['S']
        dias_de_incapacidad=item['dias_de_incapacidad']['S']
        fecha= item['fecha']['S']
        id_usuario=item['id_usuario']['N']
        id_doctor= item['id_doctor']['N']
        observaciones= item['observaciones']['S']
        print (f"""identificacion: {identificacion}, descripcion: {descripcion}, dias_de_incapacidad: {dias_de_incapacidad},
                fecha: {fecha}, id_usuario: {id_usuario}, id_doctor: {id_doctor}, observaciones: {observaciones}           
            """)#
        content={"descripcion": descripcion, 
                "dias_de_incapacidad": dias_de_incapacidad,
                "id_usuario": id_usuario, "id_doctor": id_doctor, "observaciones": observaciones, "fecha": fecha}
        payload=[]
        payload.append(content)
        return(payload)
        
#payload[]
#content {}

@router.post("/incapacidad")
async def incapacidad(user: Incapacidad):
    print ("------------------", user)
    fecha= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    identificacion = f"{user.id_usuario}{int(time.time())}"
    nuevo_registro = {
        'identificacion': {'N': identificacion},
        'descripcion': {'S': user.descripcion},
        'dias_de_incapacidad': {'S': user.dias_de_incapacidad},
        'fecha': {'S': fecha},
        'id_usuario': {'N':str(user.id_usuario)},#
        'id_doctor': {'N': str(user.id_doctor)},
        'observaciones': {'S':user.observaciones}
    }
    
    response = dynamodb.put_item(
    TableName= nombre_tabla,
    Item= nuevo_registro        
    )
    return{"resultado": "usuario registrado"}





