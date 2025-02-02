import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.user_model import Login, Token
from fastapi.encoders import jsonable_encoder
from typing import List
from datetime import datetime, timedelta
import jwt

SECRET_KEY = "fsdfsdfsdfsdfs"

class TokenController:
    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
            to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
        return encoded_jwt

    
    def generate_token(self, user: Login):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario where estado!=0 AND usuario = %s AND password = %s",(user.usuario, user.password,))
        result = cursor.fetchall()
        if result:
            access_token_expires = timedelta(minutes=50)
            access_token = self.create_access_token(data={"sub": user.usuario}, expires_delta=access_token_expires)
            return {"access_token": access_token}
        else:
            return {"message": "Credenciales incorrectas"}
    

    def verify_token(self, token: Token):
        try:
          payload = jwt.decode(token.token, SECRET_KEY, algorithms=["HS256"])
          return {"message": "Token valido"}
        except jwt.ExpiredSignatureError:
            return {"message": "Token expirado"}
        except jwt.InvalidTokenError:
            return {"message": "Token invalido"}