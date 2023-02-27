#Calculo del centro de gravedad de los cubos

def Calcular_cdg_cubos(numero_cargas_pago_new, data_new):
    
    #Creacion variables 
    if numero_cargas_pago_new != 1:
        x_cg = []
        y_cg = []
        z_cg = []
        masas = []
        masa_total_CP = 0

        for i in range(1,numero_cargas_pago_new):
            x1 = float(data_new[i]["x"])*10
            y1 = float(data_new[i]["y"])*10
            h_off = float(data_new[i]["h_off"])*10
            l_pad = float(data_new[i]["l_pad"])*10
            long_lado_h = float(data_new[i]["long_lado_h"])*10
            long_lado_v = float(data_new[i]["long_lado_v"])*10
            masa = float(data_new[i]["masa"])

            x_cg_masa = (x1+(x1+long_lado_h))/2
            x_cg.append(x_cg_masa)
            y_cg_masa = (y1+(y1+long_lado_v))/2
            y_cg.append(y_cg_masa)
            z_cg_masa = (h_off+(h_off+l_pad))/2
            z_cg.append(z_cg_masa)

            #Calculo de la masa total
            masas.append(masa)
            masa_total_CP = masa + masa_total_CP

        #Calculo CDG total de las cargas de pago
        num_x_cdg_CP = 0
        num_y_cdg_CP = 0
        num_z_cdg_CP = 0
        index = 0
        for masa in masas:
            num_x_cdg_CP = masa*x_cg[index] + num_x_cdg_CP
            num_y_cdg_CP = masa*y_cg[index] + num_y_cdg_CP
            num_z_cdg_CP = masa*z_cg[index] + num_z_cdg_CP
            index = index + 1

        x_cdg_CP = num_x_cdg_CP/masa_total_CP #En "globales" antes de constraints
        y_cdg_CP = num_y_cdg_CP/masa_total_CP
        z_cdg_CP = num_z_cdg_CP/masa_total_CP

        x_cdg_CP_corregido = x_cdg_CP + 167.676 #En "globales" tras constraints
        y_cdg_CP_corregido = y_cdg_CP + 132.385
        z_cdg_CP_corregido = z_cdg_CP + 174.662

        print("La coordenada x del centro de gravedad de la carga de pago es: " + str(x_cdg_CP))
        print("La coordenada y del centro de gravedad de la carga de pago es: " + str(y_cdg_CP))
        print("La coordenada z del centro de gravedad de la carga de pago es: " + str(z_cdg_CP))

        print("La coordenada x del centro de gravedad de la carga de pago corregida es: " + str(x_cdg_CP_corregido))
        print("La coordenada y del centro de gravedad de la carga de pago corregida es: " + str(y_cdg_CP_corregido))
        print("La coordenada z del centro de gravedad de la carga de pago corregida es: " + str(z_cdg_CP_corregido))
    else:
        print("No hay cargas de pago")

    resultados_cdg_cubos = [masa_total_CP, x_cdg_CP_corregido, y_cdg_CP_corregido, z_cdg_CP_corregido]

    return resultados_cdg_cubos