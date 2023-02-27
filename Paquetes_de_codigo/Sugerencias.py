##SUGERENCIAS REQUERIDAS

def escribir_sugerencias(x_cdg_dron, y_cdg_dron, z_cdg_dron, masa_total_CP, x_cdg_dron_cesar, y_cdg_dron_cesar, z_cdg_dron_cesar):

  sugerencia_CDG = "El centro de gravedad del dron debería estar en torno a ( " + str(x_cdg_dron/10) + ", " + str(y_cdg_dron/10) + ", " + str(z_cdg_dron/10) + " ). "
  
  if masa_total_CP == 6.505:
    sugerencia_MPL = "El peso de la carga de pago introducida coincide con el máximo admitido."
  elif masa_total_CP > 6.505:
    sugerencia_MPL = "Ha superado el peso máximo de la carga de pago admisible. La carga de pago elegida no es viable."
  else:
    sugerencia_MPL = "No ha alcanzado el peso máximo admitido para la carga de pago. Se pueden introducir " + str(6.505-masa_total_CP) + " kg más. La carga de pago elegida es viable."

  if x_cdg_dron_cesar == 43.7995339057:
    sugerencia1 = "El centro de gravedad del dron cargado coincide con el del dron sin cargar en x. "
  elif x_cdg_dron_cesar < 43.7995339057:
    sugerencia1 = "El centro de gravedad del dron cargado está retrasado en x. "
  else:
    sugerencia1 = "El centro de gravedad del dron cargado está adelantado en x. "

  if y_cdg_dron_cesar == 15.0729493536:
    sugerencia2 = "El centro de gravedad del dron cargado coincide con el del dron sin cargar en y. "
  elif y_cdg_dron_cesar > 15.0729493536:
    sugerencia2 = "El centro de gravedad del dron cargado se desplaza hacia la izquierda en y (referencia cola). "
  else: 
    sugerencia2 = "El centro de gravedad del dron cargado se desplaza hacia la derecha en y (referencia cola). "

  if z_cdg_dron_cesar == 14.362378218:
    sugerencia3 = "El centro de gravedad del dron cargado coincide con el del dron sin cargar en z. "
  elif z_cdg_dron_cesar < 14.362378218:
    sugerencia3 = "El centro de gravedad del dron cargado se desplaza hacia abajo en z. "
  else:
    sugerencia3 = "El centro de gravedad del dron cargado se desplaza hacia arriba en z. "

  sugerencia_final = sugerencia_CDG + "\n" + sugerencia1 +"\n" + sugerencia2 +"\n" + sugerencia3 +"\n" + sugerencia_MPL

  return sugerencia_final