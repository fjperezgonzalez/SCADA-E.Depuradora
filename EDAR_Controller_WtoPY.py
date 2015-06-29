



# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import math
import datetime
import serial
import time


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

@service.json
def prueba_conexion_http():
    diccionario = {'valor': 0}
    valor_mandado = request.vars.valor
    valor_mandado = str(valor_mandado)

    try:
        temp=open('/home/fjperezgonzalez/web2py/applications/init/static/E_Conexion.txt','w')
        temp.write(valor_mandado)
        temp.close()
    except:
        pass
    try:
        datos=open('/home/fjperezgonzalez/web2py/applications/init/static/E_Conexion.txt','r')
        #print "acceso txt"
        valor=datos.read()
        #print("punto 81",valores)
        datos.close()
    except:
        valor="1500"  		#valor aleatorio si falla la apertura
    valor=int(valor)
    if valor_mandado == '1':
        try:
            temp = open('/home/fjperezgonzalez/web2py/applications/init/static//Datos_Siemens.txt','w')
            #print ("PUNTO ESCRITURA ", operando1)
            estado1=0
            estado1=str(estado1)
            temp.write(estado1)
            temp.close()
        except:
            pass
        try:
            temp = open('/home/fjperezgonzalez/web2py/applications/init/static/Velocidad_inversa.txt','w')
            #print ("PUNTO ESCRITURA ", operando1)
            estado2=30000
            estado2=str(estado2)
            temp.write(estado2)
            temp.close()
        except:
            pass
        try:
            temp = open('/home/fjperezgonzalez/web2py/applications/init/static/Datos_salidas_Siemens.txt','w')
            #print ("PUNTO ESCRITURA ", operando1)
            estado3='000000000000000000000000'
            temp.write(estado3)
            temp.close()
        except:
            pass
        try:
            temp = open('/home/fjperezgonzalez/web2py/applications/init/static/Datos_entradas_Siemens.txt','w')
            #print ("PUNTO ESCRITURA ", operando1)
            estado4='0000000000000000000000000000'
            temp.write(estado4)
            temp.close()
        except:
            pass
        try:
            temp = open('/home/fjperezgonzalez/web2py/applications/init/static/Datos_Siemens_2.txt','w')
            #print ("PUNTO ESCRITURA ", operando1)
            estado5=0
            estado5=str(estado5)
            temp.write(estado5)
            temp.close()
        except:
            pass

    #print("PUNTO CONFLICTIVO ")
    valor_mandado = int(valor_mandado)
    diccionario = {'valor': valor_mandado}
    #print("El diccionario es: ",diccionario)

    return request.vars.valor

def prueba_conexion():
    diccionario = {'valor': 0}
    try:
        datos=open('/home/fjperezgonzalez/web2py/applications/init/static/E_Conexion.txt','r')
        #print "acceso txt"
        valor=datos.read()
        #print("punto 81",valores)
        datos.close()
    except:
        pass  		#valor aleatorio si falla la apertura
    valor = int(valor)
    diccionario = {'valor' : valor}
    return response.json(diccionario)

@service.json
def recogida_datos_http():



    cadena = request.vars.velocidad

    try:
        temp = open('/home/fjperezgonzalez/web2py/applications/init/static/Datos_Siemens.txt', 'w')
        temp.write(cadena)
        temp.close()
    except:
        pass


    #return request.vars.Nombre
    return request.vars.velocidad


def recogida_datos():

    """Funcion temporizada que te abre un txt que contiene los datos mandados desde la pantalla de Omron
       """
    #print "recogida datos"
    diccionario = {'valores': 0}
    try:
        datos=open('/home/fjperezgonzalez/web2py/applications/init/static/Datos_Siemens.txt','r')
        #print "acceso txt"
        valores=datos.read()
        #print("punto 81",valores)
        datos.close()
    except:
        valores="1500"          #valor aleatorio si falla la apertura
    lon_cadena = len(valores)
    #print("medida la cadena")
    if lon_cadena>2:
        #print("La longitud de la cadena es: ",lon_cadena)
        valores = int(valores)
        diccionario['valores'] = valores

    else:
        diccionario['valores'] = 100000        #Si lee un valor erroneo del txt le damos 1500 para que no se mueva la barra_if_

    #print("PUNTO CONFLICTIVO ")
    diccionario = {'valores': valores}
    #print("El diccionario es: ",diccionario)
    return response.json(diccionario)

@service.json
def recogida_datos2_http():



    cadena = request.vars.velocidad

    try:
        temp = open('/home/fjperezgonzalez/web2py/applications/init/static/Velocidad_inversa.txt', 'w')
        temp.write(cadena)
        temp.close()
    except:
        pass


    #return request.vars.Nombre
    return request.vars.velocidad

def recogida_datos2():

    """Funcion temporizada que te abre un txt que contiene los datos mandados desde la pantalla de Omron
       """
    #print "recogida datos"
    diccionario = {'valores': 0}
    try:
        datos=open('/home/fjperezgonzalez/web2py/applications/init/static/Velocidad_inversa.txt','r')
        #print "acceso txt"
        valores=datos.read()
        #print("punto 81",valores)
        datos.close()
    except:
        valores="1500"          #valor aleatorio si falla la apertura
    lon_cadena = len(valores)
    #print("medida la cadena")
    if lon_cadena>2:
        #print("La longitud de la cadena es: ",lon_cadena)
        valores = int(valores)
        diccionario['valores'] = valores

    else:
        diccionario['valores'] = 100000        #Si lee un valor erroneo del txt le damos 1500 para que no se mueva la barra_if_

    #print("PUNTO CONFLICTIVO ")
    diccionario = {'valores': valores}
    #print("El diccionario es: ",diccionario)
    return response.json(diccionario)

@service.json
def recogida_salidas_http():



    cadena = ''.join([request.vars.al_gener_plc,request.vars.s3,request.vars.pas_agua_tanque,request.vars.out_bivalva,request.vars.nivel_max_p_gruesos,request.vars.ventilador_1,request.vars.biodisco1,request.vars.biodisco2,request.vars.biodisco3,request.vars.alarm_vent,request.vars.alarm_desbaste,request.vars.alarm_tamices,request.vars.alarm_soplantes,request.vars.al_rec_solidos,request.vars.alarm_biodiscos,request.vars.al_rec_grasas,request.vars.alarm_obst_extr,request.vars.alarm_decantador,request.vars.al_obstr_bomba,request.vars.soplantes,request.vars.alarm_fangos,request.vars.bomba_extraccion,request.vars.motor_decantador,request.vars.bomba_fangos])

    try:
        temp = open('/home/fjperezgonzalez/web2py/applications/init/static/Datos_salidas_Siemens.txt', 'w')
        temp.write(cadena)
        temp.close()
    except:
        pass


    #return request.vars.Nombre
    return request.vars.al_gener_plc


def recogida_salidas():

    """Funcion temporizada que te abre un txt que contiene los datos de salidas PLC Siemens
       """
    diccionario = {'s3': 0,'al_gener_plc': 0,'out_bivalva': 0,'nivel_max_p_gruesos': 0,'ventilador_1': 0,'biodisco1': 0,'biodisco2': 0,'biodisco3': 0,'alarm_vent':0,'alarm_desbaste':0,'alarm_tamices':0,'alarm_soplantes':0,'al_rec_solidos':0,'alarm_biodiscos':0,'al_rec_grasas':0,'alarm_obst_extr':0,'alarm_decantador':0,'pas_agua_tanque': 0,'al_obstr_bomba': 0,'soplantes': 0,'alarm_fangos': 0,'motor_decantador': 0,'bomba_fangos': 0}
    try:
        datos=open('/home/fjperezgonzalez/web2py/applications/init/static/Datos_salidas_Siemens.txt','r')
        valores=datos.read()
        datos.close()
    except:
        valores="1500"          #valor aleatorio si falla la apertura
    lon_cadena = len(valores)
    #print("valores salida es",valores)
    if lon_cadena>2:
            #print("cadena de salida adecuada")
            #print("La posicion 0 de valores salidas es",valores[0])
            if valores[1]=='1':
                diccionario['s3']=1
            if valores[1]=='0':
                diccionario['s3']=0
            if valores[2]=='1':
                diccionario['pas_agua_tanque']=1
            if valores[2]=='0':
                diccionario['pas_agua_tanque']=0
            if valores[0]=='1':
                diccionario['al_gener_plc']=1
            if valores[0]=='0':
                diccionario['al_gener_plc']=0
            if valores[3]=='1':
                diccionario['out_bivalva']=1
            if valores[3]=='0':
                diccionario['out_bivalva']=0
            if valores[4]=='1':
                diccionario['nivel_max_p_gruesos']=1
            if valores[4]=='0':
                diccionario['nivel_max_p_gruesos']=0
            if valores[5]=='1':
                diccionario['ventilador_1']=1
            if valores[5]=='0':
                diccionario['ventilador_1']=0
            if valores[6]=='1':
                diccionario['biodisco1']=1
            if valores[6]=='0':
                diccionario['biodisco1']=0
            if valores[7]=='1':
                diccionario['biodisco2']=1
            if valores[7]=='0':
                diccionario['biodisco2']=0
            if valores[8]=='1':
                diccionario['biodisco3']=1
            if valores[8]=='0':
                diccionario['biodisco3']=0
            if valores[9]=='1':
                diccionario['alarm_vent']=1
            if valores[9]=='0':
                diccionario['alarm_vent']=0
            if valores[10]=='1':
                diccionario['alarm_desbaste']=1
            if valores[10]=='0':
                diccionario['alarm_desbaste']=0
            if valores[11]=='1':
                diccionario['alarm_tamices']=1
            if valores[11]=='0':
                diccionario['alarm_tamices']=0
            if valores[12]=='1':
                diccionario['alarm_soplantes']=1
            if valores[12]=='0':
                diccionario['alarm_soplantes']=0
            if valores[13]=='1':
                diccionario['al_rec_solidos']=1
            if valores[13]=='0':
                diccionario['al_rec_solidos']=0
            if valores[14]=='1':
                diccionario['alarm_biodiscos']=1
            if valores[14]=='0':
                diccionario['alarm_biodiscos']=0
            if valores[15]=='1':
                diccionario['al_rec_grasas']=1
            if valores[15]=='0':
                diccionario['al_rec_grasas']=0
            if valores[16]=='1':
                diccionario['alarm_obst_extr']=1
            if valores[16]=='0':
                diccionario['alarm_obst_extr']=0
            if valores[17]=='1':
                diccionario['alarm_decantador']=1
            if valores[17]=='0':
                diccionario['alarm_decantador']=0
            if valores[18]=='1':
                diccionario['al_obstr_bomba']=1
            if valores[18]=='0':
                diccionario['al_obstr_bomba']=0
            if valores[19]=='1':
                diccionario['soplantes']=1
            if valores[19]=='0':
                diccionario['soplantes']=0
            if valores[20]=='1':
                diccionario['alarm_fangos']=1
            if valores[20]=='0':
                diccionario['alarm_fangos']=0
            if valores[21]=='1':
                diccionario['bomba_extraccion']=1
            if valores[21]=='0':
                diccionario['bomba_extraccion']=0
            if valores[22]=='1':
                diccionario['motor_decantador']=1
            if valores[22]=='0':
                diccionario['motor_decantador']=0
            if valores[23]=='1':
                diccionario['bomba_fangos']=1
            if valores[23]=='0':
                diccionario['bomba_fangos']=0
            #print("El diccionario de salidas es: ",diccionario)
    else:
        diccionario['s3'] = 100000        #Si lee un valor erroneo del txt le damos 100000 para que no se mueva la barra_if_


    return response.json(diccionario)


@service.json
def recogida_entradas_http():



    cadena = ''.join([request.vars.p1,request.vars.p2,request.vars.s1,request.vars.s4,request.vars.s5,request.vars.s6,request.vars.s7,request.vars.s8,request.vars.s9,request.vars.s10,request.vars.s11,request.vars.s12,request.vars.s13,request.vars.act_ventiladores,request.vars.s14,request.vars.s15,request.vars.s16,request.vars.s17,request.vars.s19,request.vars.s20,request.vars.act_biodiscos,request.vars.s22,request.vars.s23,request.vars.s24,request.vars.s25,request.vars.s26,request.vars.cuch_bivalva,request.vars.orden_soplantes])

    try:
        temp = open('/home/fjperezgonzalez/web2py/applications/init/static/Datos_entradas_Siemens.txt', 'w')
        temp.write(cadena)
        temp.close()
    except:
        pass


    #return request.vars.Nombre
    return request.vars.act_ventiladores

def recogida_entradas():

    """Funcion temporizada que te abre un txt que contiene los datos de entradas PLC Siemens
       """
    diccionario = {'p1': 0,'p2': 0,'s1': 0,'s4': 0,'s5': 0,'s6': 0,'s7': 0,'s8': 0,'s9': 0,'s10': 0,'s11':0,'s12':0,'s13':0,'act_ventiladores':0,'s14':0,'s15':0,'s16':0,'s17':0,'s19':0,'s20':0,'act_biodiscos':0,'s22':0,'s23':0,'s24':0,'s25':0,'bomba_fangos':0,'s26':0,'cuch_bivalva':0}
    try:
        datos=open('/home/fjperezgonzalez/web2py/applications/init/static/Datos_entradas_Siemens.txt','r')
        valores=datos.read()
        datos.close()
    except:
        valores="1500"          #valor aleatorio si falla la apertura
    lon_cadena = len(valores)
    #print("valores entrada es",valores)
    if lon_cadena>2:
            #print("cadena de entrada adecuada")
            #print("La posicion 0 de valores entradas es",valores[0])
            if valores[0]=='1':
                diccionario['p1']=1
            if valores[0]=='0':
                diccionario['p1']=0
            if valores[1]=='1':
                diccionario['p2']=1
            if valores[1]=='0':
                diccionario['p2']=0
            if valores[2]=='1':
                diccionario['s1']=1
            if valores[2]=='0':
                diccionario['s1']=0
            if valores[3]=='1':
                diccionario['s4']=1
            if valores[3]=='0':
                diccionario['s4']=0
            if valores[4]=='1':
                diccionario['s5']=1
            if valores[4]=='0':
                diccionario['s5']=0
            if valores[5]=='1':
                diccionario['s6']=1
            if valores[5]=='0':
                diccionario['s6']=0
            if valores[6]=='1':
                diccionario['s7']=1
            if valores[6]=='0':
                diccionario['s7']=0
            if valores[7]=='1':
                diccionario['s8']=1
            if valores[7]=='0':
                diccionario['s8']=0
            if valores[8]=='1':
                diccionario['s9']=1
            if valores[8]=='0':
                diccionario['s9']=0
            if valores[9]=='1':
                diccionario['s10']=1
            if valores[9]=='0':
                diccionario['s10']=0
            if valores[10]=='1':
                diccionario['s11']=1
            if valores[10]=='0':
                diccionario['s11']=0
            if valores[11]=='1':
                diccionario['s12']=1
            if valores[11]=='0':
                diccionario['s12']=0
            if valores[12]=='1':
                diccionario['s13']=1
            if valores[12]=='0':
                diccionario['s13']=0
            if valores[13]=='1':
                diccionario['act_ventiladores']=1
            if valores[13]=='0':
                diccionario['act_ventiladores']=0
            if valores[14]=='1':
                diccionario['s14']=1
            if valores[14]=='0':
                diccionario['s14']=0
            if valores[15]=='1':
                diccionario['s15']=1
            if valores[15]=='0':
                diccionario['s15']=0
            if valores[16]=='1':
                diccionario['s16']=1
            if valores[16]=='0':
                diccionario['s16']=0
            if valores[17]=='1':
                diccionario['s17']=1
            if valores[17]=='0':
                diccionario['s17']=0
            if valores[18]=='1':
                diccionario['s19']=1
            if valores[18]=='0':
                diccionario['s19']=0
            if valores[19]=='1':
                diccionario['s20']=1
            if valores[19]=='0':
                diccionario['s20']=0
            if valores[20]=='1':
                diccionario['act_biodiscos']=1
            if valores[20]=='0':
                diccionario['act_biodiscos']=0
            if valores[21]=='1':
                diccionario['s22']=1
            if valores[21]=='0':
                diccionario['s22']=0
            if valores[22]=='1':
                diccionario['s23']=1
            if valores[22]=='0':
                diccionario['s23']=0
            if valores[23]=='1':
                diccionario['s24']=1
            if valores[23]=='0':
                diccionario['s24']=0
            if valores[24]=='1':
                diccionario['s25']=1
            if valores[24]=='0':
                diccionario['s25']=0
            if valores[25]=='1':
                diccionario['s26']=1
            if valores[25]=='0':
                diccionario['s26']=0
            if valores[26]=='1':
                diccionario['cuch_bivalva']=1
            if valores[26]=='0':
                diccionario['cuch_bivalva']=0
            '''
            if valores[28]=='1':
                diccionario['orden_soplantes']=1
            if valores[28]=='0':
                diccionario['orden_soplantes']=0


                '''

            #print("El diccionario de entradas es: ",diccionario)
    else:
        diccionario['p1'] = 100000        #Si lee un valor erroneo del txt le damos 100000 para que no se mueva la barra_if_


    return response.json(diccionario)


def recibe_datos_http():
    diccionario = {'valor': 0}
    try:
        datos=open('/home/fjperezgonzalez/web2py/applications/init/static/Datos_Siemens_2.txt','r')
        valor=datos.read()
        datos.close()
    except:
        pass
    valor = int(valor)
    diccionario = {'valor' : valor}
    return valor



def recibe_datos():
    diccionario = {'valores': 0}
    operando1=int(request.vars.operando1)
    try:
        temp = open('/home/fjperezgonzalez/web2py/applications/init/static/Datos_Siemens_2.txt','w')
        #print ("PUNTO ESCRITURA ", operando1)
        operando1=str(operando1)
        temp.write(operando1)
        temp.close()
    except:
        pass
    return diccionario





def pide_hora():
    hora=datetime.datetime.now().strftime("%H:%M:%S")
    fecha=datetime.datetime.now().strftime("%d-%m-%Y")
    return dict(hora=hora,fecha=fecha)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
