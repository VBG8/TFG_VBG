#CALCULO DEL CDG DEL DRON + CARGAPAGO

def Calcular_cdg_total(numero_cargas_pago_new, masa_total_CP, masa_total_dron, x_cdg_dron, y_cdg_dron, z_cdg_dron, x_cdg_CP_corregido, y_cdg_CP_corregido, z_cdg_CP_corregido):

    if numero_cargas_pago_new != 1:
        masa_CP_DRON = masa_total_CP + masa_total_dron
        x_cdg_total = (x_cdg_dron*masa_total_dron + x_cdg_CP_corregido*masa_total_CP)/masa_CP_DRON
        y_cdg_total = (y_cdg_dron*masa_total_dron + y_cdg_CP_corregido*masa_total_CP)/masa_CP_DRON
        z_cdg_total = (z_cdg_dron*masa_total_dron + z_cdg_CP_corregido*masa_total_CP)/masa_CP_DRON
    else:
        x_cdg_total = x_cdg_dron
        y_cdg_total = y_cdg_dron
        z_cdg_total = z_cdg_dron
    
    resultado_cdg_total = [x_cdg_total, y_cdg_total, z_cdg_total]

    return resultado_cdg_total