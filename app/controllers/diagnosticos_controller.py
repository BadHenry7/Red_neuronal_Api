import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.diagnosticos_model import Diagnosticos, Reportesss
from fastapi.encoders import jsonable_encoder

class diagnosticoController:
        
    def create_diagnosticos(self, diagnosticos: Diagnosticos):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO diagnosticos (id_cita,resultado,descripcion,Observacion,estado) VALUES (%s,%s,%s,%s,%s)", (diagnosticos.id_cita, diagnosticos.resultado,diagnosticos.descripcion,diagnosticos.Observacion,diagnosticos.estado,))
            cursor.execute("""
                UPDATE cita 
                SET estado = 0
                WHERE id = %s    
                """, (diagnosticos.id_cita,))
            conn.commit()
            conn.close()
            return {"resultado": "diagnosticos añadida correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            print ("error", err)
            raise HTTPException(status_code=500, detail="Error")  
        finally:
            conn.close()
        

    def get_diagnostico(self, diagnosticos_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM diagnosticos WHERE id = %s", (diagnosticos_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_usuario':int(result[1]),
                    'resultado':str(result[2]),
                    'fecha_diagnostico':str(result[3]),
                    'estado':bool(result[4]),
                  
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="diagnostico not find")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_diagnosticos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM diagnosticos")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_usuario':data[1],
                    'resultado':data[2],
                    'fecha_diagnostico':data[3],
                    'estado':data[4],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="diagnosticos not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def update_diagnosticos(self, diagnosticos_id: int, diagnosticos: Diagnosticos):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE diagnosticos
            SET id_usuario = %s,
            resultado = %s,
            fecha_diagnostico = %s,
            estado = %s 
            WHERE id = %s
            """,(diagnosticos.id_usuario, diagnosticos.resultado, diagnosticos.fecha_diagnostico,diagnosticos.estado,diagnosticos_id,))
            conn.commit()
           
            return {"resultado": "Diagnosticos actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   
       
    def delete_diagnosticos(self, diagnosticos_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM diagnosticos WHERE id = %s',(diagnosticos_id,))
            conn.commit()           
            return {"resultado": "Diagnosticos eliminado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    


    
    def reportes_diagnosticos(self, diagnosticos: Reportesss):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                           
            SELECT diagnosticos.resultado, diagnosticos.fecha_diagnostico, paciente.nombre AS nombre_paciente
            FROM diagnosticos
            INNER JOIN usuario AS paciente 
            INNER JOIN cita ON cita.id_paciente = paciente.id AND diagnosticos.id_cita = cita.id
            WHERE diagnosticos.fecha_diagnostico BETWEEN %s AND %s
                           """,(diagnosticos.fecha, diagnosticos.fecha2))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'resultado':data[0],
                    'fecha_diagnostico':str(data[1]),
                    'nombre_paciente':data[2],
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
    
   