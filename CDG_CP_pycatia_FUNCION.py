#Funcion que calcula CDG de la CARGA DE PAGO, del DRON, el CDG_TOTAL y crea el STL de las CARGAS DE PAGO

def Calculo_cdg(data_new):

  ##Antes de utilizar este código, se recomienda asegurarse de que las siguientes RUTAS son correctas

  #OJO, después de un "\" no escribir "t" o "n" pues "\t" es TABULACIÓN y "\n" es SALTO DE LÍNEA; 
  # si escribo "t" o "n" y quiero que el caracter de cadena se entienda de manera LITERAL, entonces debo
  # escribir "r" delante del STRING. Para ver la explicación: https://es.stackoverflow.com/questions/442488/qu%C3%A9-significa-la-letra-r-precediendo-una-constante-de-cadena

  rutas_JSON = r"C:\CATIA\Diseño Dron\MI_TFG\Todo_Virgi\Mi_TFG_Final"
  ruta_STLs = r"C:\CATIA\Diseño Dron\MI_TFG\Todo_Virgi\Mi_TFG_Final\ArchivosSTL"
  rutas_CARGAS = r"C:\CATIA\Diseño Dron\MI_TFG\Todo_Virgi\Ensamble definitivo dron"
  ruta_CDG_cargado = rutas_CARGAS

  #Librerias importadas
  from pycatia import catia 
  from pycatia.enumeration.enumeration_types import cat_constraint_type, cat_constraint_mode, cat_constraint_orientation
  from pycatia.enumeration.enumeration_types import cat_work_mode_type  #Importo el modulo de trabajo de catia en el product
  from os import remove
  from shutil import move
  from Paquetes_de_codigo.Borrar_cargas_antiguas import borrar_cargas
  from Paquetes_de_codigo.Crear_PART_cargas import Crear_cargas_pago
  from Paquetes_de_codigo.Calcular_CDG_cubos import Calcular_cdg_cubos
  from Paquetes_de_codigo.RenovarJSON import Renovar_json
  from Paquetes_de_codigo.Sugerencias import escribir_sugerencias
  from Paquetes_de_codigo.Calcular_CDG_dron import Calcular_cdg_dron
  from Paquetes_de_codigo.Calcular_CDG_cargas_y_dron import Calcular_cdg_total
  from Paquetes_de_codigo.Correcciones_del_CDG import Corregir_CDG
  from Paquetes_de_codigo.Creacion_CDG_dron_CARGADO import Crear_CDG_dron_CARGADO
  from Paquetes_de_codigo.Creacion_de_STLs import Creacion_de_STLs

  #Importacion JSON VIEJO
  import json
  with open(rutas_JSON + "\datos_viejos.json") as componente:
    data_viejos = json.load(componente) 
  
  numero_cargas_pago_old = int(data_viejos[0]["numero_cargas"]) + 1

  #Se borran las cargas de pago antiguas de Catia
  borrar_cargas(data_viejos, numero_cargas_pago_old, catia, rutas_CARGAS)

  #Se crea el PART con las cargas de pago definidas
  numero_cargas_pago_new = Crear_cargas_pago(catia, data_new, cat_constraint_type, cat_constraint_mode, rutas_CARGAS)

  #Se calcula el CDG del PART de los cubos
  [masa_total_CP, x_cdg_CP_corregido, y_cdg_CP_corregido, z_cdg_CP_corregido] = Calcular_cdg_cubos(numero_cargas_pago_new, data_new)

  #Renovación del archivo JSON
  Renovar_json(move, remove, data_new, rutas_JSON)

  #CODIGO QUE OPERA EN EL DRON CALCULANDO EL CDG
  [masa_total_dron, x_cdg_dron, y_cdg_dron, z_cdg_dron] = Calcular_cdg_dron(catia, cat_work_mode_type, rutas_CARGAS)

  #CALCULO DEL CDG DEL DRON + CARGAPAGO
  [x_cdg_total, y_cdg_total, z_cdg_total] = Calcular_cdg_total(numero_cargas_pago_new, masa_total_CP, masa_total_dron, x_cdg_dron, y_cdg_dron, z_cdg_dron, x_cdg_CP_corregido, y_cdg_CP_corregido, z_cdg_CP_corregido)

  #COORDENADAS FINALES PARA CESAR CORREGIDAS CON LOS EJES QUE ÉL QUIERE EN [CM]
  [x_cdg_dron_cesar, y_cdg_dron_cesar, z_cdg_dron_cesar, x_cdg_total_cesar, y_cdg_total_cesar, z_cdg_total_cesar] = Corregir_CDG(x_cdg_dron, y_cdg_dron, z_cdg_dron, x_cdg_total, y_cdg_total, z_cdg_total)

  ##Codigo que crea el cubo que muestra el CDG del DRON CARGADO
  Crear_CDG_dron_CARGADO(catia, x_cdg_total, y_cdg_total, z_cdg_total, cat_constraint_type, cat_constraint_mode, ruta_CDG_cargado)

  ##VISUALIZACION DE LAS CARGAS DE PAGO DENTRO DEL DRON Y CREACION DE STLs
  Creacion_de_STLs(catia, cat_constraint_type, cat_constraint_orientation, rutas_CARGAS, ruta_CDG_cargado, ruta_STLs)

  ##SUGERENCIAS REQUERIDAS
  sugerencia_final = escribir_sugerencias(x_cdg_dron, y_cdg_dron, z_cdg_dron, masa_total_CP, x_cdg_dron_cesar, y_cdg_dron_cesar, z_cdg_dron_cesar)
  print(sugerencia_final)

  #Envío de resultados a la página web
  coordenadas_CDG = [x_cdg_dron_cesar, y_cdg_dron_cesar, z_cdg_dron_cesar, x_cdg_total_cesar, y_cdg_total_cesar, z_cdg_total_cesar, sugerencia_final]
  
  print(x_cdg_dron, " " , x_cdg_dron_cesar, " ", y_cdg_dron, " ", y_cdg_dron_cesar, " ", z_cdg_dron, " ", z_cdg_dron_cesar)
  print(x_cdg_total, " " , x_cdg_total_cesar, " ", y_cdg_total, " ", y_cdg_total_cesar, " ", z_cdg_total, " ", z_cdg_total_cesar)
  
  return coordenadas_CDG

def Calcular_AyA(datos_AyA):

  import math

  #Calculo de la AUTONOMIA

  I_other = float(datos_AyA[0]["Corriente_max_equipos"])
  I_motor = float(datos_AyA[0]["Corriente_max_1motor"])
  N_motor = float(datos_AyA[0]["Numero_motores"])
  L_flying = float(datos_AyA[0]["Carga_vuelo"])
  Q = float(datos_AyA[0]["Capacidad_bateria"])
  C_rate = float(datos_AyA[0]["Tasa_C_bateria"])
  V_batnominal = float(datos_AyA[0]["Tension_nominal_bateria"])
  Regla_descarga = float(datos_AyA[0]["Regla_descarga_bateria"])
  Regla_descarga_bateria = Regla_descarga/100

  I_maxfull_load = I_other+I_motor*N_motor
  I_flyingload = I_maxfull_load*L_flying
  tiempo_vuelo = (((Q/1000)/I_flyingload)*60)*Regla_descarga_bateria
  N_bat_requeridas = math.ceil(I_maxfull_load/((Q*C_rate)/1000))
  Pot_maxima = I_maxfull_load*V_batnominal

  #Calculo del ALCANCE

  vel_vuelo = float(datos_AyA[0]["Velocidad_vuelo"])
  velocidad_vuelo = vel_vuelo/60
  alcance = velocidad_vuelo*tiempo_vuelo

  resultado_AyA = [tiempo_vuelo, alcance]
  
  return resultado_AyA