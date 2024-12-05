import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.rol_model import Rol
from fastapi.encoders import jsonable_encoder

class RolController:
        
    def create_rol(self, rol: Rol):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO rol (nombre,descripcion,estado) VALUES (%s, %s,%s)", (rol.nombre, rol.descripcion, rol.estado,))
            conn.commit()
            conn.close()
            return {"resultado": "Rol creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_rol(self, rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rol WHERE id = %s", (rol_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'descripcion':result[2],
                    'estado':bool(result[3])
                  
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="rol not creado")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_roles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rol")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'descripcion':data[2],
                    'estado':data[3]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def update_rol(self, rol_id: int, rol: Rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE rol
            SET nombre = %s,
            descripcion = %s,
            estado = %s 
            WHERE id = %s
            """,(rol.nombre, rol.descripcion,rol.estado,rol_id,))
            conn.commit()
           
            return {"resultado": "Rol actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   
       
    def delete_rol(self, rol_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM rol WHERE id = %s',(rol_id,))
            conn.commit()           
            return {"resultado": "Rol eliminado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    #
    
    
       

##user_controller = UserController()           que nervlos