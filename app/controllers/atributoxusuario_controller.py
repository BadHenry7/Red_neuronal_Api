import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.atributoxusuario_model import Atributoxusuario, BuscarAtributoxusuario,UpdateAtributoxusuario
from fastapi.encoders import jsonable_encoder

class AtributoxusuarioController:
        
    def create_atributoxusuario(self, atributoxusuario: Atributoxusuario):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO atrixusuario (id_usuario,id_atributo,valor,descripcion,estado) VALUES (%s,%s,%s,%s,%s)",(atributoxusuario.id_usuario, atributoxusuario.id_atributo,atributoxusuario.valor,atributoxusuario.descripcion,atributoxusuario.estado,))
            conn.commit()
            conn.close()
            return {"resultado": "Atributoxusuario ingresado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_atributoxusuario(self, atributoxusuario: BuscarAtributoxusuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor() #mano ya vengo dale
            cursor.execute("SELECT * FROM atrixusuario WHERE id_usuario = %s", (atributoxusuario.id_usuario,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_usuario':int(result[1]),
                    'id_atributo':int(result[2]),
                    'valor':result[3],
                    'descripcion':result[4],
                    'estado':bool(result[5])
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Atributoxusuario not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_atributoxusuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atrixusuario")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_usuario':data[1],
                    'id_atributo':data[2],
                    'valor':data[3],
                    'descripcion':data[4],
                    'estado':data[5],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="not atributesxusuario founds")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    

    def update_atributoxusuarios(self, atributoxusuario_id: int, atributoxusuario: Atributoxusuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE atrixusuario
            SET id_usuario=%s,
            id_atributo = %s,
            valor = %s,
            descripcion = %s,
            estado = %s
            WHERE id = %s
            """,(atributoxusuario.id_usuario, atributoxusuario.id_atributo,atributoxusuario.valor,atributoxusuario.descripcion,atributoxusuario.estado,atributoxusuario_id,))
            conn.commit()
           
            return {"resultado": "Todo actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    


    def delete_atributoxusuarios(self, atributoxusuario_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM atrixusuario WHERE id = %s',(atributoxusuario_id,))
            conn.commit()           
            return {"resultado": "atrixusuario eliminado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def updateatributoxusuario(self, atributoxusuario: UpdateAtributoxusuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE atrixusuario
            SET valor = %s,
            descripcion=%s
            WHERE id_usuario = %s
            """,(atributoxusuario.valor, atributoxusuario.descripcion, atributoxusuario.id_usuario,))
            conn.commit()
           
            return {"resultado": "Usuario actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()  
##atributexusuario_controller = AtributoController()