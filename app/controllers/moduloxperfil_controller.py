import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.moduloxperfil_model import *
from fastapi.encoders import jsonable_encoder

class ModuloxPerfilController:

    def create_moduloxperfil (self, moduloxperfil: ModuloxPerfil):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()   
            print("moduloxperfilssssssssssssssssssssssssssssss")
            cursor.execute("SELECT id from modulo")
            rv=cursor.fetchall()

            print(moduloxperfil)

            
            for result in rv:
                id_modulo_v=result[0]
                print ("-------------------------------------------1",result)   
                cursor.execute("INSERT INTO moduloxperfil (id_rol,id_modulo,estado) VALUES (%s,%s,%s)", (moduloxperfil.id_rol,id_modulo_v,0,))
                conn.commit()


            for result in moduloxperfil.id_modulo:
                print ("-------------------------------------------2",result)   
                cursor.execute("""
                             UPDATE moduloxperfil AS mx
                            SET estado = 1
                            WHERE id_rol = %s AND id_modulo=%s   
                        """,(moduloxperfil.id_rol, result))
                conn.commit()
            conn.close()
            id=cursor.lastrowid
            return {id}#aja

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_moduloxperfil(self, moduloxperfil: Buscar_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor() 
            cursor.execute("SELECT * FROM moduloxperfil WHERE id_modulo = %s", (moduloxperfil.id_modulo,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_rol':int(result[1]),
                    'id_modulo':int(result[2]),
                    'estado': bool(result[3]),
                    'create':result[4],
                    'update':result[5],
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="moduloxperfil not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def get_mxp_id(self, moduloxperfil: Buscar_id_rol):#buscar id_rol
        try:
            conn = get_db_connection()
            cursor = conn.cursor() 
            cursor.execute("""SELECT mxp.id_modulo, mxp.estado 
                           FROM moduloxperfil as mxp
                           inner join rol as r ON mxp.id_rol=r.id
                           WHERE r.id =%s
                           
                           
                           """, (moduloxperfil.id_rol,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for rv in result:
                content={
                        'id_modulo':int(rv[0]),
                        'estado':str(rv[1])

                }
                payload.append(content)
                
            
            json_data = jsonable_encoder(payload)            
            if result:
               return  {"resultado":json_data}
            else:
                raise HTTPException(status_code=404, detail="moduloxperfil not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()       

    def get_modulosxperfil(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor() 
            cursor.execute("SELECT * FROM moduloxperfil")
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_rol':int(result[1]),
                    'id_modulo':int(result[2]),
                    'estado': bool(result[3]),
                    'create':result[4],
                    'update':result[5],
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="modulosxperfil not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def update_moduloxperfil (self, moduloxperfil: ModuloxPerfil):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE moduloxperfil
            SET id_rol = %s,
            id_modulo=%s,
            estado =%s 
            WHERE id = %s
            """,(moduloxperfil.id_rol,moduloxperfil.id_modulo,moduloxperfil.estado,moduloxperfil.id,))
            conn.commit()
           
            return {"resultado": "Moduloxperfil actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def desactivar_moduloxperfil (self, moduloxperfil: Buscar_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE modulo
            SET
            estado =  0                
            WHERE id = %s
            """,(moduloxperfil.id,))
            conn.commit()
           
            return {"resultado": "moduloxperfil desactivado correctamente :c"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()