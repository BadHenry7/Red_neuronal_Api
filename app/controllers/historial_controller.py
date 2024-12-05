import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.historial_model import Historial,Reportesss
from fastapi.encoders import jsonable_encoder

class historial_Controller:
        
    def create_historial(self, historial: Historial):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO historial (id_usuario,id_sintoma,fecha,estado) VALUES (%s,%s,%s,%s)", (historial.id_usuario,historial.id_sintoma,historial.fecha, historial.estado,))
            conn.commit()
            conn.close()
            return {"resultado": "historial añadido correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_historial(self, historial_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM historial WHERE id = %s", (historial_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_usuario':int(result[1]),
                    'id_sintoma':int(result[2]),
                    'fecha':str(result[3]),
                    'estado':bool(result[4]),
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="historial not find")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

       
    def get_historiales(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM historial")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_usuario':data[1],
                    'id_sintoma':data[2],
                    'fecha':data[3],
                    'estado':data[4],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="historiales not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def update_historial(self, historial_id: int, historial: Historial):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE historial
            SET id_usuario = %s,
            id_sintoma = %s,
            fecha = %s,
            estado = %s
            WHERE id = %s
            """,(historial.id_usuario, historial.id_sintoma, historial.fecha, historial.estado,historial_id,))
            conn.commit()
           
            return {"resultado": "historial actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   

       
    def delete_historial(self, historial_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM historial WHERE id = %s',(historial_id,))
            conn.commit()           
            return {"resultado": "historial eliminado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    
    def reportes_historial(self, historial: Reportesss):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
           SELECT usuario.nombre as Nombre, COUNT(cita.id_paciente) AS numero_citas, MAX(cita.fecha) AS Ultimodiagnostio
        FROM usuario
        INNER JOIN cita as cita on cita.id_paciente=usuario.id
        WHERE cita.fecha BETWEEN %s AND %s
        GROUP BY cita.id_paciente
                           """,(historial.fecha, historial.fecha2))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'nombre':data[0],
                    'numero_citas':str(data[1]),
                    'Ultimodiagnostio':data[2],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
               
            else:
                raise HTTPException(status_code=404, detail="citas not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    

    