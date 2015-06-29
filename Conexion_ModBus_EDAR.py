

import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import time
import httplib, urllib
import smtplib

#######  Programa maestro que comunica mediante protocolo Modbus un automata esclavo Siemens S7 1200

if __name__ == "__main__":
    try:
        #Conectamos con el esclavo
		master = modbus_tcp.TcpMaster(port=5000,host="192.168.0.1")
		velocidad = ""
		estado_boton = ""
		print ("Intentando conectar...")
		
		#####  Si no hay problemas para conectar, escribimos un 0 en E_Conexion.txt
		
		try:
			temp = open('/home/francisco/web2py/applications/prueba_svg_anim/static/E_Conexion.txt','w')
			estado = 0
			estado = str(0)
			temp.write(estado)
			temp.close()
		except:
			pass
		
		#####  Le enviamos a la pagina web la senal de que la conexion esta correcta mediante 'valor': 0	
			
		try:
			params7 = urllib.urlencode({'valor': 0})
			headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
			#headers = {"Content-type": "text/html","Accept":"text/plain"}  
			conn = httplib.HTTPConnection("fjperezgonzalez.pythonanywhere.com")
			conn.request("POST", "http://fjperezgonzalez.pythonanywhere.com/init/default/prueba_conexion_http" ,params7,headers)
			response7=conn.getresponse()
			print ("Lo que recibe la pagina es : ",response7.read())
		except:
			pass
			   
		while True:
			####### Leemos el registro de entrada de agua bruta, que es un valor analogico
			
			print ("Entramos en el bucle")
			print master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 1)
			nivel = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 1)
			nivel_bueno = nivel[0]
			nivel_bueno = str(nivel_bueno)
				
			params3 = urllib.urlencode({'velocidad': nivel_bueno})
			
			####  Mandamos el valor a la pagina web
			
			conn = httplib.HTTPConnection("fjperezgonzalez.pythonanywhere.com")
			conn.request("POST", "http://fjperezgonzalez.pythonanywhere.com/init/default/recogida_datos_http" ,params3,headers)
			response3=conn.getresponse()
			#print ("Lo que recibe la pagina es : ",response3.read())
			
			####   Escribimos tambien en el txt para el modo local 
			
			try:
				temp = open('/home/francisco/web2py/applications/prueba_svg_anim/static/Datos_Siemens.txt','w')
				temp.write(nivel_bueno)
				temp.close()
			except:
				pass
				
			####   Leemos un txt(de la pagina) que nos indica si hemos introducido un valor desde pagina web para cambio de velocidad
			params8 = urllib.urlencode({'velocidad': nivel_bueno})	####	Esto no importa		
			conn = httplib.HTTPConnection("fjperezgonzalez.pythonanywhere.com")
			conn.request("POST", "http://fjperezgonzalez.pythonanywhere.com/init/default/recibe_datos_http" ,params8,headers)
			response8=conn.getresponse()
			#print ("Lo que recibe la pagina es : ",response8.read())
			velocidad = response8.read()			
			print ("VELOCIDAD ES IGUAL A : ",velocidad)
			velocidad = int(velocidad)										
			'''	
			try:
				temp = open('/home/francisco/web2py/applications/prueba_svg_anim/static/Datos_Siemens_2.txt','r')
				velocidad = temp.read()
				velocidad = int(velocidad)
				temp.close()
			except:
				pass
			'''	
			####    Escribimos en el registro correspondiente para el cambio de velocidad
				
			master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 1, output_value=([0,velocidad]))
			MW104 = master.execute(1, cst.READ_HOLDING_REGISTERS, 2, 1)
			print ("MW104 es igual a ",MW104)
								
			####	Leemos las salidas y las guardamos en un txt como cadena de ceros y unos
			
			s3_aux = master.execute(1, cst.READ_COILS,0,45)
			s3 = s3_aux[1]
			s3 = str(s3)
									
			al_gener_plc = s3_aux[0]
			al_gener_plc = str(al_gener_plc)
									
			out_bivalva= s3_aux[3]
			out_bivalva = str(out_bivalva)
			
			nivel_max_p_gruesos= s3_aux[4]
			nivel_max_p_gruesos = str(nivel_max_p_gruesos)
			
			ventilador_1= s3_aux[6]
			ventilador_1= str(ventilador_1)
			
			biodisco1= s3_aux[29]
			biodisco1= str(biodisco1)
			
			biodisco2= s3_aux[30]
			biodisco2= str(biodisco2)
			
			biodisco3= s3_aux[31]
			biodisco3= str(biodisco3)
			
			alarm_vent= s3_aux[16]
			alarm_vent= str(alarm_vent)
			
			alarm_desbaste= s3_aux[6]
			alarm_desbaste= str(alarm_desbaste)
			
			alarm_tamices= s3_aux[7]
			alarm_tamices= str(alarm_tamices)
			
			alarm_soplantes= s3_aux[25]
			alarm_soplantes= str(alarm_soplantes)
			
			al_rec_solidos= s3_aux[20]
			al_rec_solidos= str(al_rec_solidos)
			
			alarm_biodiscos= s3_aux[32]
			alarm_biodiscos= str(alarm_biodiscos)
			
			al_rec_grasas= s3_aux[28]
			al_rec_grasas= str(al_rec_grasas)
			
			alarm_obst_extr= s3_aux[27]
			alarm_obst_extr= str(alarm_obst_extr)
			
			alarm_decantador= s3_aux[34]
			alarm_decantador= str(alarm_decantador)
			
			pas_agua_tanque = s3_aux[2]
			pas_agua_tanque = str(pas_agua_tanque)
			
			al_obstr_bomba = s3_aux[5]
			al_obstr_bomba = str(al_obstr_bomba)
			
			soplantes = s3_aux[24]
			soplantes = str(soplantes)
			
			alarm_fangos = s3_aux[36]
			alarm_fangos = str(alarm_fangos)
			
			bomba_extraccion= s3_aux[26]
			bomba_extraccion= str(bomba_extraccion)
			
			motor_decantador= s3_aux[33]
			motor_decantador= str(motor_decantador)
			
			bomba_fangos= s3_aux[35]
			bomba_fangos= str(bomba_fangos)
			
			
			datos_salidas = ''.join([al_gener_plc,s3,pas_agua_tanque,out_bivalva,nivel_max_p_gruesos,ventilador_1,biodisco1,biodisco2,biodisco3,alarm_vent,alarm_desbaste,alarm_tamices,alarm_soplantes,al_rec_solidos,alarm_biodiscos,al_rec_grasas,alarm_obst_extr,alarm_decantador,al_obstr_bomba,soplantes,alarm_fangos,bomba_extraccion,motor_decantador,bomba_fangos])
			
			#####	Le mandamos a la pagina las salidas en formato diccionario
			
			params = urllib.urlencode({'s3': int(s3),'al_gener_plc': int(al_gener_plc),'out_bivalva': int(out_bivalva),'nivel_max_p_gruesos': int(nivel_max_p_gruesos),'ventilador_1': int(ventilador_1),'biodisco1': int(biodisco1),'biodisco2': int(biodisco2),'biodisco3': int(biodisco3),'alarm_vent':int(alarm_vent),'alarm_desbaste':int(alarm_desbaste),'alarm_tamices':int(alarm_tamices),'alarm_soplantes':int(alarm_soplantes),'al_rec_solidos':int(al_rec_solidos),'alarm_biodiscos':int(alarm_biodiscos),'al_rec_grasas':int(al_rec_grasas),'alarm_obst_extr':int(alarm_obst_extr),'alarm_decantador':int(alarm_decantador),'pas_agua_tanque': int(pas_agua_tanque),'al_obstr_bomba':int(al_obstr_bomba),'soplantes': int(soplantes),'alarm_fangos': int(alarm_fangos),'bomba_extraccion': int(bomba_extraccion),'motor_decantador': int(motor_decantador),'bomba_fangos': int(bomba_fangos)})
			conn = httplib.HTTPConnection("fjperezgonzalez.pythonanywhere.com")
			conn.request("POST", "http://fjperezgonzalez.pythonanywhere.com/init/default/recogida_salidas_http" ,params,headers)
			response=conn.getresponse()
			#print ("Lo que recibe la pagina es : ",response.read())
			
			####   Escribimos tambien en el txt para el modo local 
			
			try:
				temp = open('/home/francisco/web2py/applications/prueba_svg_anim/static/Datos_salidas_Siemens.txt','w')
				temp.write(datos_salidas)
				temp.close()
			except:
				pass
				
			####	Leemos las entradas y las guardamos en un txt como cadena de ceros y unos
			
			entradas_aux = master.execute(1, cst.READ_DISCRETE_INPUTS,0,40)
			p1 = entradas_aux[0]
			p1 = str(p1)
						
			p2 = entradas_aux[1]
			p2= str(p2)
			
			s1 = entradas_aux[2]
			s1 = str(s1)
			
			s4 = entradas_aux[3]
			s4 = str(s4)			
			
			s5= entradas_aux[4]
			s5 = str(s5)
			
			s6= entradas_aux[5]
			s6= str(s6)

			s7= entradas_aux[6]
			s7= str(s7)
	
			s8= entradas_aux[7]
			s8= str(s8)
			
			s9= entradas_aux[8]
			s9= str(s9)
			
			s10= entradas_aux[9]
			s10= str(s10)
			
			cuch_bivalva= entradas_aux[10]
			cuch_bivalva= str(cuch_bivalva)
			
			s11= entradas_aux[11]
			s11= str(s11)
			
			s12= entradas_aux[12]
			s12= str(s12)
			
			s13= entradas_aux[13]
			s13= str(s13)
			
			act_ventiladores= entradas_aux[16]
			act_ventiladores= str(act_ventiladores)
			
			s14= entradas_aux[17]
			s14= str(s14)
			
			s15= entradas_aux[18]
			s15= str(s15)
			
			s16= entradas_aux[19]
			s16= str(s16)
			
			orden_soplantes= entradas_aux[20]
			orden_soplantes= str(orden_soplantes)
			
			s17= entradas_aux[21]
			s17= str(s17)
			
			s19= entradas_aux[23]
			s19= str(s19)
			
			s20= entradas_aux[24]
			s20= str(s20)
			
			act_biodiscos= entradas_aux[25]
			act_biodiscos= str(act_biodiscos)
			
			s22= entradas_aux[26]
			s22= str(s22)
			
			s23= entradas_aux[27]
			s23= str(s23)
			
			s24= entradas_aux[28]
			s24= str(s24)
			
			s25= entradas_aux[30]
			s25= str(s25)
						
			s26= entradas_aux[32]
			s26= str(s26)		
			
			datos_entradas = ''.join([p1,p2,s1,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,act_ventiladores,s14,s15,s16,s17,s19,s20,act_biodiscos,s22,s23,s24,s25,s26,cuch_bivalva,orden_soplantes])
			
			#####	Le mandamos a la pagina las entradas en formato diccionario
			
			params2 = urllib.urlencode({'p1': p1,'p2': p2,'s1': s1,'s4': s4,'s5': s5,'s6': s6,'s7': s7,'s8': s8,'s9': s9,'s10': s10,'s11':s11,'s12':s12,'s13':s13,'act_ventiladores':act_ventiladores,'s14':s14,'s15':s15,'s16':s16,'s17':s17,'s19':s19,'s20':s20,'act_biodiscos':act_biodiscos,'s22':s22,'s23':s23,'s24':s24,'s25':s25,'s26':s26,'cuch_bivalva':cuch_bivalva,'orden_soplantes':orden_soplantes}) 
			conn = httplib.HTTPConnection("fjperezgonzalez.pythonanywhere.com")
			conn.request("POST", "http://fjperezgonzalez.pythonanywhere.com/init/default/recogida_entradas_http" ,params2,headers)
			response2=conn.getresponse()
			#print ("Lo que recibe la pagina es : ",response2.read())
							
			####   Escribimos tambien en el txt para el modo local 
				
			try:
				temp = open('/home/francisco/web2py/applications/prueba_svg_anim/static/Datos_entradas_Siemens.txt','w')
				temp.write(datos_entradas)
				temp.close()
			except:
				pass

			####	Leemos un registro cuyo valor nos indicara que la potencia aplicada a una bomba debe ser inversamente proporcional al caudal
			
			velocidad_inversa = master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 1)			
			print ("velocidad_inversa es igual a",velocidad_inversa)
			vel_inv = velocidad_inversa[0]
			vel_inv = str(vel_inv)
			
			#####	Le mandamos a la pagina el valor en formato diccionario
			
			params4 = urllib.urlencode({'velocidad': vel_inv}) 
			conn = httplib.HTTPConnection("fjperezgonzalez.pythonanywhere.com")
			conn.request("POST", "http://fjperezgonzalez.pythonanywhere.com/init/default/recogida_datos2_http" ,params4,headers)
			response4=conn.getresponse()
			#print ("Lo que recibe la pagina es : ",response4.read())
			
			####   Escribimos tambien en el txt para el modo local 
			
			try:
				temp = open('/home/francisco/web2py/applications/prueba_svg_anim/static/Velocidad_inversa.txt','w')
				temp.write(vel_inv)
				temp.close()
			except:
				pass
				
			time.sleep(2)
	
	####	A continuacion vienen las excepciones que se ejecutan cuando hay un fallo en la conexion
        
    except modbus_tk.modbus.ModbusError, e:
        print "Modbus error ", e.get_exception_code()
     
	####	Si se produce un error en la conexion, mandamos un email indicando que hay un fallo en la instalacion
	####	"MENSAJE" contiene todo lo que contiene el email, y el formato con el que se manda
        
	MENSAJE = """From: EDAR <panch287@gmail.com>
	To: To Person <to@todomain.com>
	MIME-Version: 1.0
	Content-type: text/html
	Subject: HA HABIDO UN FALLO EN LA INSTALACION

	<h1>Averia.</h1>
	Ha habido un fallo en la alimentacion y/o un error de conexion. Por favor revise la instalacion.


	"""	

	####	Al ser gmail debemos poner 587
	
	try:
		mail = smtplib.SMTP('smtp.gmail.com',587)
		mail.ehlo()
		mail.starttls()
		mail.login('panch287@gmail.com','pancho06200')   ####	Email que envia y password
		mail.sendmail('panch287@gmail.com','fjperezgonzalez0@gmail.com',MENSAJE)####	Origen, destino y mensaje
		mail.close()
	except:
		pass

	####	Tanto en modo local como en la pagina web debemos indicar que se ha producido un error de conexion
		
	try:
		temp = open('/home/francisco/web2py/applications/prueba_svg_anim/static/E_Conexion.txt','w')
		estado = 1
		estado = str(1)
		temp.write(estado)
		temp.close()
		params6 = urllib.urlencode({'valor': 1}) 
		conn = httplib.HTTPConnection("fjperezgonzalez.pythonanywhere.com")
		conn.request("POST", "http://fjperezgonzalez.pythonanywhere.com/init/default/prueba_conexion" ,params6,headers)
		response6=conn.getresponse()
	except:
		pass
			  
    except Exception, e2:
        print "Error ", str(e2)
	MENSAJE = """From: EDAR <panch287@gmail.com>
		To: To Person <to@todomain.com>
		MIME-Version: 1.0
		Content-type: text/html
		Subject: HA HABIDO UN FALLO EN LA INSTALACION

		<h1>Averia.</h1>
		Ha habido un fallo en la alimentacion y/o un error de conexion. Por favor revise la instalacion.


		"""	
	try:
		mail = smtplib.SMTP('smtp.gmail.com',587)
		mail.ehlo()
		mail.starttls()
		mail.login('panch287@gmail.com','pancho06200')
		mail.sendmail('panch287@gmail.com','fjperezgonzalez0@gmail.com',MENSAJE)

		mail.close()
	except:
		pass
	

	try:
		temp = open('/home/francisco/web2py/applications/prueba_svg_anim/static/E_Conexion.txt','w')
		estado = 1
		estado = str(1)
		temp.write(estado)
		temp.close()
		params6 = urllib.urlencode({'valor': 1}) 
		conn = httplib.HTTPConnection("fjperezgonzalez.pythonanywhere.com")
		conn.request("POST", "http://fjperezgonzalez.pythonanywhere.com/init/default/prueba_conexion_http" ,params6,headers)
		response6=conn.getresponse()	
	except:
		pass
     
