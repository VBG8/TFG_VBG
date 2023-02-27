#CODIGO QUE OPERA EN EL DRON CALCULANDO EL CDG

def Calcular_cdg_dron(catia, cat_work_mode_type, rutas_CARGAS):

  caa = catia()
  documents = caa.documents
  documents.open(rutas_CARGAS + "\Ensamblaje del dron.CATProduct")

  document = caa.active_document
  product = document.product

  #Change the work mode to Design Mode.
  product.apply_work_mode(cat_work_mode_type.index("DESIGN_MODE"))

  def print_properties(obj):
      print(f"{obj.name}: mass: {obj.analyze.mass}, \n"
            f"    volume: {obj.analyze.volume}, \n"
            f"    gravity_center: {obj.analyze.get_gravity_center()}, \n"
            )

  products = product.products

  if len(products) == 0:
      print("Active document has no children or is not a CATProduct.")

  #Prueba que me verifica que el CDG esta bien calculado con los bucles inferiores
  # prueba = product.analyze.get_gravity_center()
  # print(prueba)

  #Definicion de variables como arrays vacios
  v_nombres = []
  v_masas = []
  v_cdg_x = []
  v_cdg_y = []
  v_cdg_z = []

  for product in products:
      if product.is_catpart():
          product.activate_default_shape()  #activa la opcion por defecto
          v_nombres.append(product.name)
          v_masas.append(product.analyze.mass)
          v_cdg_pieza = product.analyze.get_gravity_center()
          v_cdg_x.append(v_cdg_pieza[0])
          v_cdg_y.append(v_cdg_pieza[1])
          v_cdg_z.append(v_cdg_pieza[2])

  #Calculo de la masa total del dron para posterior calculo de CDG
  masa_total_dron = 0
  for i in range(0,len(v_masas)):
      masa_total_dron = v_masas[i] + masa_total_dron

  #Calculo del centro de gravedad por coordenadas
  #COORDENADA X, Y, Z
  num_x_cdg_dron = 0  
  num_y_cdg_dron = 0
  num_z_cdg_dron = 0
  indice = 0
  for mass in v_masas:
      x_cdg = v_cdg_x[indice]
      y_cdg = v_cdg_y[indice]
      z_cdg = v_cdg_z[indice]
      num_x_cdg_dron = mass*x_cdg + num_x_cdg_dron
      num_y_cdg_dron = mass*y_cdg + num_y_cdg_dron
      num_z_cdg_dron = mass*z_cdg + num_z_cdg_dron
      indice = indice + 1

  x_cdg_dron = num_x_cdg_dron/masa_total_dron
  y_cdg_dron = num_y_cdg_dron/masa_total_dron
  z_cdg_dron = num_z_cdg_dron/masa_total_dron

  resultados_cdg_dron = [masa_total_dron, x_cdg_dron, y_cdg_dron, z_cdg_dron]

  return resultados_cdg_dron