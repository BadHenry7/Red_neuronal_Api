import mysql.connector
from fastapi import HTTPException, UploadFile
from app.config.db_config import get_db_connection
from app.models.user_model import *
from fastapi.encoders import jsonable_encoder
from typing import List
import pandas as pd

class UserController:
    
    def create_user(self, user: User):   
        try:
            print("111111111111111", user)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE usuario= %s  ||  documento= %s", (user.usuario,user.documento))
            result = cursor.fetchall()

            if result:
               
                content = {}    
                content={"Informacion":"Ya_existe"}
              
                return jsonable_encoder(content)
            else:   
                cursor.execute("INSERT INTO usuario (usuario,password,nombre,apellido,documento,telefono,id_rol,estado, genero, edad) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (user.usuario,user.password,user.nombre,user.apellido,user.documento,user.telefono,user.id_rol,user.estado, user.genero, user.edad,))
                conn.commit()
                conn.close()
                id=cursor.lastrowid
                return {id}#aja

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def create_user_masivo (self, file: UploadFile):
        conn = None
        try:
            # Leer el archivo Excel
            df = pd.read_excel(file.file, engine='openpyxl')

            required_columns = ['usuario', 'password', 'nombre', 'apellido', 'documento', 'telefono', 'id_rol', 'estado']
            for col in required_columns:
                if col not in df.columns:
                    return {"error": f"Falta la columna: {col}"}
            
            # Conectar a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            for index, row in df.iterrows():
                cursor.execute(
                    "INSERT INTO usuario (usuario,password,nombre,apellido,documento,telefono,id_rol,estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                    (row['usuario'], row['password'], row['nombre'], row['apellido'], row['documento'], row['telefono'], row['id_rol'], row['estado'])
                )
            
            conn.commit()  # Hacer commit después de todas las inserciones
            return {"resultado": "Users creados exitosamente"}
        except mysql.connector.Error as err:
            if conn:
                conn.rollback()  # Asegúrate de que conn esté definido
            return {"error": str(err)}
        except Exception as e:
            if conn:
                conn.rollback()
            return {"error": f"Un error inesperado ocurrió: {str(e)}"}
        finally:
            if conn:
                conn.close()

    
    def get_user(self, user: Buscar):
        
        try:
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT usuario.*, rol.*
                FROM usuario
                JOIN rol ON usuario.id_rol = rol.id
                        WHERE usuario.id=%s """, (user.id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'usuario':result[1],
                    'password':result[2],
                    'nombre':result[3],
                    'apellido':result[4],
                    'documento':result[5],
                    'telefono':result[6],
                    'id_rol':int(result[7]),
                    'estado':bool(result[8]),
                    'roles_name':result[14],
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

    def get_user_document(self, user: Buscar_document):
        
        try:
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE documento = %s ", (user.documento,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'usuario':result[1],
                    'password':result[2],
                    'nombre':result[3],
                    'apellido':result[4],
                    'documento':result[5],
                    'telefono':result[6],
                    'id_rol':int(result[7]),
                    'estado':bool(result[8]),
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
       

    def get_users(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT usuario.*, rol.*
                FROM usuario
                JOIN rol ON usuario.id_rol = rol.id
                        WHERE usuario.id_rol!=1;

                           
                           
                           """)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'usuario':data[1],
                    'password':data[2],
                    'nombre':data[3],
                    'apellido':data[4],
                    'documento':data[5],
                    'telefono':data[6],
                    'id_rol':data[7],
                    'estado':data[8],

                    'nombre_rol':data[14],
                   

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

    def get_medicos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id_rol=3")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'usuario':data[1],
                    'password':data[2],
                    'nombre':data[3],
                    'apellido':data[4],
                    'documento':data[5],
                    'telefono':data[6],
                    'id_rol':data[7],
                    'estado':data[8]
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


    def get_paciente(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario where id_rol=2")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'usuario':data[1],
                    'password':data[2],
                    'nombre':data[3],
                    'apellido':data[4],
                    'documento':data[5],
                    'telefono':data[6],
                    'id_rol':data[7],
                    'estado':data[8]
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

    def get_medico(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario where id_rol=3")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'usuario':data[1],
                    'password':data[2],
                    'nombre':data[3],
                    'apellido':data[4],
                    'documento':data[5],
                    'telefono':data[6],
                    'id_rol':data[7],
                    'estado':data[8]
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

       
    def update_user(self, user: Actualizar):
        try:
            print("user", user)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE usuario
            SET usuario = %s,
            nombre=%s,
            apellido = %s,
            documento=%s,
            telefono=%s ,
            id_rol=%s,
            estado =%s,
            genero=%s,
            edad=%s, 
            password=%s
            WHERE id = %s
            """,(user.usuario,user.nombre,user.apellido,user.documento,user.telefono,user.id_rol,user.estado,user.genero, user.edad,user.password,user.id,))
            conn.commit()
           
            return {"resultado": "Usuario actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    

             
    def update_adm(self, adm: ActualizarAdm):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE usuario
            SET usuario = %s,
            nombre=%s,
            apellido = %s,
            documento=%s,
            password=%s,                           
            telefono=%s
            WHERE id = %s
            """,(adm.usuario,adm.nombre,adm.apellido,adm.documento,adm.password,adm.telefono,adm.id,))
            conn.commit()
           
            return {"resultado": "Usuario actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    

        
    def delete_user(self, user_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM usuario WHERE id = %s',(user_id,))
            conn.commit()           
            return {"resultado": "Usuario eliminado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def login(self, user: Login):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario where estado!=0 AND usuario = %s AND password = %s",(user.usuario, user.password,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'usuario':data[1],
                    'password':data[2],
                    'nombre':data[3],
                    'id':data[0],
                    'rol':data[7],


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


    def verif_user(self, user: Verif_user):   
        try:
            print("111111111111111", user)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE usuario= %s ", (user.usuario,))

            result = cursor.fetchone()

            if result:
                
                content = {}    
                content={"Informacion":"Ya_existe", 'id':int(result[0]),'rol_v':int(result[7]), 'estado':bool(result[8]), }
              
                return jsonable_encoder(content)
            else:   
                cursor.execute("SELECT * FROM sesiongoogle where google_id = %s",(user.google_id,))

                result= cursor.fetchone()
                
                if result:
                    content = {}    
                    content={"Informacion":"Ya_existe_google"}
                    return jsonable_encoder(content)

                else:
                    print ("*--------**-/*/",user)
                    cursor.execute("INSERT INTO usuario (usuario,password,nombre,apellido,documento,telefono,id_rol,estado, genero, edad) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (user.usuario,"LOGINadminLOGIN1",user.nombre,user.apellido,"google_id","000000",2,0, "genero", 0,))
                    id=cursor.lastrowid
                    cursor.execute("INSERT INTO sesiongoogle (id_usuario, google_id, access_token, foto, estado) VALUES (%s, %s, %s, %s,%s)",
                               (id, user.google_id, user.access_token,user.foto,user.estado,))
                    conn.commit()
                   
                    content = {}    
                    content={"Informacion":"Registrada", 'id': id}
                    return jsonable_encoder(content)


        except mysql.connector.Error as err:
            conn.rollback()
            print(f"Error en la base de datos: {err}")  
        finally:
            conn.close() 






  
    def verificar_usuario(self, user: login_google):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sesiongoogle where google_id = %s",(user.verif_user.google_id,))
            result = cursor.fetchone()
            if result:
               print("-------------")
               return {"resultado": "usuario ya registrado"}
            else:
                print("-----------------2")
                user_id=self.create_user(user.user)
                print("Usuario registrando", user_id)
                cursor.execute("INSERT INTO sesiongoogle (id_usuario, google_id, access_token, foto, estado) VALUES (%s, %s, %s, %s,%s)",
                               (user_id, user.verif_user.google_id, user.verif_user.access_token,user.verif_user.foto,))
                return {"resultado": "usuario registrado"}             
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    # try: 
        
    #     # Buscar si el usuario ya existe en la BD
    #     #const [rows] = await db.execute('SELECT * FROM usuarios WHERE google_id = ?', [google_id]);

    #     if (rows.length > 0) {
    #         console.log("Usuario ya registrado:", rows[0]);
    #         return res.json(rows[0]);  // Si existe, devolver sus datos
    #     } else {
    #         console.log("Nuevo usuario, registrándolo en la BD...");
    #         await db.execute('INSERT INTO usuarios (google_id,     access_token) VALUES (?, ?, ?, ?, ?)', 
    #             [google_id, nombre, email, foto, access_token]);

    #         return res.json({ google_id, nombre, email, foto });
    #     }
 




    def estado_user(self, user: Estado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE usuario
            SET
            estado =  %s                
            WHERE id = %s
            """,(user.estado,user.id,))
            conn.commit()
           
            return {"resultado": "Usuario desactivado correctamente :c"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close() 

       

            
##user_controller = UserController()


#AFK