import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.sintomas_model import Sintomas
from fastapi.encoders import jsonable_encoder

class sintomasController:
        
    def create_sintomas(self, sintomas: Sintomas):   #

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO sintomas (nombre,descripcion,estado,id_cita) VALUES (%s,%s,%s,%s)", (sintomas.nombre, sintomas.descripcion, sintomas.estado,sintomas.id_cita))
            conn.commit()
            conn.close()
            return {"resultado": "sintoma generada correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_sintoma(self, sintomas_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sintomas WHERE id = %s", (sintomas_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'nombre':str(result[1]),
                    'descripcion':str(result[2]),
                    'estado':bool(result[3]),
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="sintoma not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_sintomas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sintomas")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'descripcion':data[2],
                    'estado':data[3],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="sintomas not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def update_sintomas(self, sintomas_id: int, sintomas: Sintomas):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE sintomas
            SET nombre = %s,
            descripcion = %s,
            estado = %s
            WHERE id = %s
            """,(sintomas.nombre, sintomas.descripcion, sintomas.estado,sintomas_id,))
            conn.commit()
           
            return {"resultado": "sintoma actualizada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   
       
    def delete_sintomas(self, sintomas_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM sintomas WHERE id = %s',(sintomas_id,))
            conn.commit()           
            return {"resultado": "sintoma eliminada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    