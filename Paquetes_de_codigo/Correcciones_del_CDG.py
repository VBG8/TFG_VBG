#COORDENADAS FINALES PARA CESAR CORREGIDAS CON LOS EJES QUE ÉL QUIERE EN [CM]

def Corregir_CDG(x_cdg_dron, y_cdg_dron, z_cdg_dron, x_cdg_total, y_cdg_total, z_cdg_total):
    
    x_cdg_dron_cesar = (x_cdg_dron - 167.68)/10     #NOTA: HAY QUE CORREGIRLOS CON RESPECTO A LOS EJES QUE HEMOS MARCADO NOSOTROS
    y_cdg_dron_cesar = (y_cdg_dron - 132.385)/10
    z_cdg_dron_cesar = (z_cdg_dron - 174.66)/10
    x_cdg_total_cesar = (x_cdg_total - 167.68)/10
    y_cdg_total_cesar = (y_cdg_total - 132.385)/10
    z_cdg_total_cesar = (z_cdg_total - 174.66)/10

    resultado_cesar = [x_cdg_dron_cesar, y_cdg_dron_cesar, z_cdg_dron_cesar, x_cdg_total_cesar, y_cdg_total_cesar, z_cdg_total_cesar]
    return resultado_cesar