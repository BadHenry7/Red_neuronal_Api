import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.modulo_model import Modelito,Modulo,Buscarid
from fastapi.encoders import jsonable_encoder

class ModuloController:

    def create_modulo (self, modulo: Modulo):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM modulo WHERE nombre= %s ", (modulo.nombre,))
            result = cursor.fetchall()

            if result:
               
                content = {}    
                content={"Informacion":"Ya_existe"}
              
                return jsonable_encoder(content)
            else:   
                cursor.execute("INSERT INTO modulo (nombre,submodulos,url,descipcion,estado) VALUES (%s,%s,%s,%s,%s)", (modulo.nombre,modulo.submodulos,modulo.url,modulo.descripcion,modulo.estado))
                conn.commit()
                conn.close()
                id=cursor.lastrowid
                return {id}#aja

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_modulo (self, modulo: Buscarid):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM modulo WHERE id = %s ", (modulo.id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'submodelos':result[2],
                    'url':result[3],
                    'descripcion':result[4],
                    'estado':bool(result[5]),
                    'create':(result[6]),
                    'update':(result[7]),
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_modulos_asignado (self, modelo: Buscarid):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(""" 
            SELECT 
                r.id as id_rol,
                r.nombre AS rol_nombre, 
                r.descripcion AS rol_descripcion, 
                r.estado AS rol_estado, 
                m.id as m_id,
                m.nombre AS modulo_nombre, 
                m.submodulos, 
                m.url, 
                m.descripcion AS modulo_descripcion
            FROM rol AS r
            INNER JOIN moduloxperfil AS mxp ON mxp.id_rol = r.id
            INNER JOIN modulo AS m ON mxp.id_modulo = m.id
            WHERE r.id = %s AND mxp.estado!=0
            ORDER BY m.nombre;
                    """, (modelo.id,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_rol': data[0],
                    'nombre':data[1],
                    'descripcion':data[2],
                    'estado_rol':data[3],
                    'id_modelo':data[4],
                    'nombre_modulo':data[5],
                    'submodulo':data[6],
                    'url':data[7],
                    'descripcion_sub':data[8],
                }
                payload.append(content)
                content = {}

            if result:
               return {"resultado": payload}
            else:
                raise HTTPException(status_code=404, detail="Modulo not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_modulos (self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM modulo")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'submodelos':data[2],
                    'url':data[3],
                    'descripcion':data[4],
                    'estado':bool(data[5]),
                    'create':(data[6]),
                    'update':(data[7]),
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Modulo not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def update_modulo (self, modulo: Modulo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE modulo
            SET nombre = %s,
            submodulos=%s,
            url=%s,
            descripcion=%s,
            estado =%s 
            WHERE id = %s
            """,(modulo.nombre,modulo.submodulos,modulo.url,modulo.descripcion,modulo.estado,modulo.id,))
            conn.commit()
           
            return {"resultado": "Modulo actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def desactivar_modulo (self, modulo: Buscarid):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE modulo
            SET
            estado =  0                
            WHERE id = %s
            """,(modulo.id,))
            conn.commit()
           
        

            return {"resultado": "modulo desactivado correctamente :c"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close() 



    def update_modulo_seleccionado (self, modulo: Modelito):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()


            if modulo.estado!=False:
                print ("------------------------------------------condicional1sas")

                cursor.execute("""
                    UPDATE rol AS r
                    JOIN moduloxperfil AS mxp ON mxp.id_rol = r.id
                    JOIN modulo AS m ON mxp.id_modulo = m.id
                    SET 
                    r.nombre = %s,         
                    r.descripcion = %s,  
                    r.estado = 1,
                    mxp.estado=0

                    WHERE r.id=%s
                """,(modulo.nombre, modulo.descripcion, modulo.id,))
                print ("------------------------------------------condicional1")
                conn.commit()
                

            else:
                cursor.execute("""
                    UPDATE rol AS r
                    JOIN moduloxperfil AS mxp ON mxp.id_rol = r.id
                    JOIN modulo AS m ON mxp.id_modulo = m.id
                    SET  
                    r.estado = 0
                    WHERE r.id=%s
                """,(modulo.id,))
                print ("------------------------------------------condicional2", modulo.id)

                conn.commit()

            print ("------------------------------------------", modulo)
            for result in modulo.modulo_seleccionado:
                cursor.execute("""
                              UPDATE moduloxperfil AS mx
                            SET estado = 1
                            WHERE id_rol = %s AND id_modulo=%s

                                    """,
                               (modulo.id,result,))
            conn.commit()   
            print ("------------------------------------------entra al for")
           
            return {"resultado": "Rol actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()



"""
  UPDATE rol AS r
                JOIN moduloxperfil AS mxp ON mxp.id_rol = r.id
                JOIN modulo AS m ON mxp.id_modulo = m.id
                SET 
                r.nombre = %s,         
                r.descripcion = %s,  
                r.estado = %s       
                WHERE r.id=%s;


"""