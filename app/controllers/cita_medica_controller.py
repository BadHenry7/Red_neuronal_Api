import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.citas_medicas_model import *
from fastapi.encoders import jsonable_encoder
from datetime import timedelta
class citaController:
        
    def create_cita(self, cita: Citasm):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cita (fecha,hora,estado,id_usuario,id_paciente, ubicacion) VALUES (%s,%s,%s,%s,%s,%s)", (cita.fecha,cita.hora,cita.estado,cita.id_usuario,cita.id_paciente, cita.ubicacion,))
            conn.commit()
            conn.close()
            return {"resultado": "Cita añadida correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_cita(self, cita_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cita WHERE id = %s", (cita_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'fecha':str(result[1]),
                    'hora':str(result[2]),
                    'estado':bool(result[3]),
                    'id_usuario':int(result[4]),
                    'id_paciente':int(result[5])
                  
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="cita not find")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
  #SELECT  nombre  FROM cita INNER JOIN usuario ON cita.id_usuario = usuario.id     
  
    def editar_cita(self, cita: EditarCita):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                           
                          SELECT cita.fecha,  cita.hora, usuario.nombre AS nombre_usuario,  paciente.nombre AS nombre_paciente, 
                           cita.id, cita.ubicacion, cita.salas, cita.id_usuario
            FROM cita
            INNER JOIN usuario AS usuario ON cita.id_usuario = usuario.id
            INNER JOIN usuario AS paciente ON cita.id_paciente = paciente.id 
            WHERE cita.id=%s """, (cita.id,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                hora_v = str(data[1])
                if len(hora_v) == 7:  # Verificar si la hora tene el formato "H:mm:ss"
                     hora_v = "0" + hora_v 
                content={
                    'fecha':data[0],
                    'hora':hora_v,
                    'medico':data[2],
                    'paciente':data[3],
                    'id':data[4],
                    'ubicacion':data[5],
                    'salas':data[6],
                    'id_usuario':data[7]




                
                }
                print(data[1])
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
    

    def get_cita_admin(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                           
                          SELECT cita.fecha,  cita.hora, usuario.nombre AS nombre_usuario,  paciente.nombre AS nombre_paciente, cita.id,
                           cita.ubicacion, cita.salas
            FROM cita
            INNER JOIN usuario AS usuario ON cita.id_usuario = usuario.id
            INNER JOIN usuario AS paciente ON cita.id_paciente = paciente.id
            WHERE cita.estado=1              
                           
                           """)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'fecha':data[0],
                    'hora':str(data[1]),
                    'medico':data[2],
                    'paciente':data[3],
                    'id':data[4],
                    'ubicacion':data[5],
                    'salas':data[6]


                
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

    def post_citas_users(self, cita: Buscar):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(""" 
                           
                           SELECT cita.fecha,  cita.hora,  usuario.nombre AS nombre_usuario,  paciente.nombre AS nombre_paciente , cita.id AS id_cita,
                           cita.ubicacion, cita.salas
                            FROM cita
                             INNER JOIN usuario AS usuario ON cita.id_usuario = usuario.id
                             INNER JOIN usuario AS paciente ON cita.id_paciente = paciente.id WHERE 
                            cita.id_paciente =%s AND cita.estado=1
                           
                           """,(cita.id_paciente,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'fecha':data[0],
                    'hora':str(data[1]),
                    'medico':data[2],
                    'paciente':data[3],
                    'id_cita':data[4],
                    'ubicacion':data[5],
                    'salas':data[6],

                
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



        
    def post_citas_doctor(self, cita: Buscar):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(""" 
                           
                           SELECT cita.fecha,  cita.hora,  usuario.nombre AS nombre_usuario,  paciente.nombre AS nombre_paciente , cita.id AS id_cita
                            FROM cita
                             INNER JOIN usuario AS usuario ON cita.id_usuario = usuario.id
                             INNER JOIN usuario AS paciente ON cita.id_paciente = paciente.id WHERE 
                            cita.id_usuario =%s AND cita.estado=1
                           
                           """,(cita.id_paciente,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'fecha':data[0],
                    'hora':str(data[1]),
                    'medico':data[2],
                    'paciente':data[3],
                    'id_cita':data[4]
                
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


    def update_cita(self, cita: Upditon):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE cita
            SET fecha = %s,
            hora = %s,
            id_usuario = %s,
            ubicacion = %s,
            salas = %s                           
            WHERE id = %s
            """,(cita.fecha,cita.hora,cita.id_usuario,cita.ubicacion, cita.salas,cita.id,))
            conn.commit()
           
            return {"resultado": "cita actualizada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   
       
    def delete_cita(self, cita: Chaocita):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('UPDATE cita SET estado=0 WHERE id =%s',(cita.id,))
            conn.commit()           
            return {"resultado": "cita eliminada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
#-------------------------------------------------------Para abajo los reportes--------------------------------------------
    
    def reportes_citas(self, cita: Reportesss):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                           
            SELECT cita.fecha, cita.hora, usuario.nombre AS nombre_usuario,  paciente.nombre AS nombre_paciente     
            FROM cita
            INNER JOIN usuario AS usuario ON cita.id_usuario = usuario.id 
            INNER JOIN usuario AS paciente ON cita.id_paciente = paciente.id 
            WHERE cita.fecha BETWEEN %s AND %s
                           """,(cita.fecha, cita.fecha2))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'fecha':data[0],
                    'hora':str(data[1]),
                    'medico':data[2],
                    'paciente':data[3]
                
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




    def reportes_citas_medicos(self, cita: Reportes_medico):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                           
            SELECT cita.fecha, cita.hora, usuario.nombre AS nombre_usuario,  paciente.nombre AS nombre_paciente     
            FROM cita
            INNER JOIN usuario AS usuario ON cita.id_usuario = usuario.id 
            INNER JOIN usuario AS paciente ON cita.id_paciente = paciente.id 
            WHERE cita.fecha BETWEEN %s AND %s AND usuario.id=%s
                           """,(cita.fecha, cita.fecha2, cita.id))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'fecha':data[0],
                    'hora':str(data[1]),
                    'medico':data[2],
                    'paciente':data[3]
                
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







#-------------------------------------------------------Para abajo las estadisticas--------------------------------------------

    def estadisticas_citas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                           
          SELECT COUNT(c.id_paciente) AS "citas", u.nombre AS "doctor"
            FROM cita c
            JOIN usuario u ON c.id_usuario = u.id
            GROUP BY u.nombre;

                           """,)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'citas':data[0], 
                    'doctor':data[1], 

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

    def estadisticas2_citas(self):#Estadisticas para saber cuantas citas hay por dia
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""                       
         SELECT  fecha  AS fecha, COUNT(*) AS citas_por_dia
         FROM cita
        GROUP BY fecha  
        ORDER BY fecha 
                           """,)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'Fecha':data[0], 
                    'citas_dia':data[1], 

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

    def estadisticas3_citas(self):#Estadisticas para saber cuantas citas hay por dia
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SET lc_time_names = 'es_ES'")
            cursor.execute("""                       
    SELECT 
    MONTHNAME(fecha) AS mes, 
    COUNT(*) AS citas_por_mes
    FROM cita
    GROUP BY mes
    ORDER BY fecha
                           """,)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'Fecha':data[0], 
                    'citas_mes':data[1], 

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


    def estadisticas4_citas(self):#Estadisticas para saber cuantas citas hay por dia
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""                       
        SELECT 
         YEAR(fecha) AS year,
         COUNT(*) AS citas_por_mes
        FROM cita
        GROUP BY  year
        ORDER BY  year
                           """,)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'Fecha':data[0], 
                    'citas_year':data[1], 

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


    def estadisticas_citas_activas(self):#Estadisticas para saber cuantas citas hay por dia
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""                       
       
            SELECT 
            MONTHNAME(fecha) AS mes, 
            COUNT(*) AS citas_por_mes
            FROM cita
            WHERE estado=1
            GROUP BY mes
            ORDER BY fecha
                           """,)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'Fecha':data[0], 
                    'citas_mes':data[1], 

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


    def estadisticas_citas_desactivado(self):#Estadisticas para saber cuantas citas hay por dia
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""                       
       
            SELECT 
            MONTHNAME(fecha) AS mes, 
            COUNT(*) AS citas_por_mes
            FROM cita
            WHERE estado=0
            GROUP BY mes
            ORDER BY fecha
                           """,)
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'Fecha':data[0], 
                    'citas_mes':data[1], 

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

    def estadisticas_avg_citas(self, cita: Reportesss):#Estadisticas para el promedio de cita
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""                       
       
         SELECT 
           MONTHNAME(fecha) AS mes, YEAR(fecha) AS years, AVG(total_citas) AS promedio_citas
        FROM (
          SELECT fecha, COUNT(*) AS total_citas
            FROM  cita
            GROUP BY 
            fecha 
        ) AS citas_por_dia
        WHERE fecha BETWEEN %s AND %s
        GROUP BY 
        years, mes 
        ORDER BY 
         years, mes

                           """,(cita.fecha, cita.fecha2, ))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'mes':data[0], 
                    'years':data[1], 
                    'promedio_citas':data[2]

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

    def historia_clinica(self, historia_clinica: Buscar):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""     
            SELECT
            cita.id, diagnosticos.fecha_diagnostico as fecha_diagnostico, 
            diagnosticos.resultado as diagnosticos, diagnosticos.descripcion, diagnosticos.observacion as "Observacion/tratamiento", sintomas.nombre as sintomas ,sintomas.descripcion as "descripcion_sintomas"
            FROM cita
            JOIN
            diagnosticos ON cita.id = diagnosticos.id_cita
            JOIN 
            usuario ON usuario.id=cita.id_paciente
            JOIN 
            sintomas ON cita.id= sintomas.id_cita
            WHERE usuario.id=%s
                           """,(historia_clinica.id_paciente,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'fecha_diagnostico':str(data[1]),
                    'diagnostico':data[2],
                    'descripcion':data[3],
                    'Observaciontratamiento':data[4],
                    'sintomas':data[5],
                    'descripcion_sintomas':data[6],         
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
    

    def historia_clinica_user(self, historia_clinica: Buscar):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""     
            SELECT
            cita.id, diagnosticos.fecha_diagnostico as fecha_diagnostico, 
            diagnosticos.resultado as diagnosticos, diagnosticos.descripcion, diagnosticos.observacion as "Observacion/tratamiento", 
            sintomas.nombre as sintomas ,sintomas.descripcion as "descripcion_sintomas", doctor.nombre
            FROM cita
            JOIN
            diagnosticos ON cita.id = diagnosticos.id_cita
            JOIN 
            usuario ON usuario.id=cita.id_paciente
            JOIN
            usuario as doctor ON doctor.id=cita.id_usuario
            JOIN 
            sintomas ON cita.id= sintomas.id_cita
            WHERE usuario.id=%s AND diagnosticos.fecha_diagnostico= ( SELECT MAX(diagnosticos.fecha_diagnostico) FROM diagnosticos);
                           """,(historia_clinica.id_paciente,))
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'fecha_diagnostico':str(data[1]),
                    'diagnostico':data[2],
                    'descripcion':data[3],
                    'Observaciontratamiento':data[4],
                    'sintomas':data[5],
                    'descripcion_sintomas':data[6],
                    'doictor':data[7],

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


    def get_ultima_cita(self, user: Buscar_cedula):
        
        try:
            print ("-----", user)
            print ("-----", user.cedula)

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT c.fecha, 
                p.nombre AS paciente_nombre, 
                p.documento AS paciente_documento, 
                d.nombre AS doctor_nombre
                FROM cita AS c
                INNER JOIN usuario AS p ON c.id_paciente = p.id
                INNER JOIN usuario AS d ON c.id_usuario = d.id
                WHERE p.documento = %s
                ORDER BY c.fecha DESC
                LIMIT 1 """, (user.cedula,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                   
                    'fecha':result[0],
                    'doctor':result[3],
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