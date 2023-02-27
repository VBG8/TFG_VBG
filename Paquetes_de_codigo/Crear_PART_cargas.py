#Se crean los prismas de las cargas de pago en el PART
#
def Crear_cargas_pago(catia, data_new, cat_constraint_type, cat_constraint_mode, rutas_CARGAS):
    
    #Abre Catia
    caa = catia()
    documents = caa.documents
    documents.open(rutas_CARGAS + "\Cargapago.CATPart")

    #Documento activo sobre el que se trabaja
    document = caa.active_document

    #Codigo que crea el prisma
    part = document.part

    #Codigo hydridbody (CREA EL BODY)
    body = part.main_body
    body.name = "Carga de pago"

    numero_cargas_pago_new = int(data_new[0]["numero_cargas"]) + 1 #Se añade una unidad porque en el archivo JSON la primera carga esta en la posicion 1 y si numero de cargas = 3, el range ira hasta 2

    for i in range(1, numero_cargas_pago_new):

        #Creacion variables 
        ##NOTA-> x1 e y1 hacen referencia a las coordenadas del punto 4 situado abajo a la izquierda

        x1 = float(data_new[i]["x"])*10 
        y1 = float(data_new[i]["y"])*10 
        h_off = float(data_new[i]["h_off"])*10 
        l_pad = float(data_new[i]["l_pad"])*10
        long_lado_h = float(data_new[i]["long_lado_h"])*10
        long_lado_v = float(data_new[i]["long_lado_v"])*10

        #CREA PLANO OFFSET
        sketches = body.sketches
        hbs = part.hybrid_bodies
        geom_set = hbs.add()
        geom_set.name = ("Construction Geometry: "+ data_new[i]["name"])
        originElements = part.origin_elements
        hsf = part.hybrid_shape_factory
        hsp = originElements.plane_xy   #(hybridShapePlaneExplicit -> hsp)
        reference = part.create_reference_from_object(hsp)
        hsp_plane_offset = hsf.add_new_plane_offset(reference, h_off, False)  #(hybridShapePlaneOffset1 -> hsp_plane_offset)
        geom_set.append_hybrid_shape(hsp_plane_offset)
        hsp_plane_offset.name = ("Plane Offset: "+ data_new[i]["name"])
        part.in_work_object = hsp_plane_offset
        part.update() 
        sketch = sketches.add(hsp_plane_offset)
        sketch.name = ("Sketch: "+ data_new[i]["name"])

        #CREA EL PRISMA
        #Abre la edicion del skecth y coloca los ejes 
        part.in_work_object = sketch
        skecth_open_edition = sketch.open_edition()  #(factory2D1 -> skecth_open_edition)
        geometricElements = sketch.geometric_elements
        absolute_axis = geometricElements.item("AbsoluteAxis") #(axis2D1 -> absolute_axis)
        h_axis = absolute_axis.get_item("HDirection")  #(line2D1 -> h_axis)
        h_axis.report_name = 1
        v_axis = absolute_axis.get_item("VDirection") #(line2D2 -> v_axis)
        v_axis.report_name = 2

        #Colocacion punto del prisma
        coord_punto_1 = skecth_open_edition.create_point(x1, y1+long_lado_v)  #(point2D1 -> coord_punto_1)
        coord_punto_1.report_name = 3
        coord_punto_1.name = "Coordenadas punto 1"
        coord_punto_2 = skecth_open_edition.create_point(x1+long_lado_h, y1+long_lado_v)  #(point2D2 -> coord_punto_2)
        coord_punto_2.report_name = 4
        coord_punto_2.name = "Coordenadas punto 2"
        linea_puntos_1_2 = skecth_open_edition.create_line(x1, y1+long_lado_v, x1+long_lado_h, y1+long_lado_v) #(line2D3 -> linea_puntos_1_2)
        linea_puntos_1_2.report_name = 5
        linea_puntos_1_2.name = "Linea union puntos 1-2"
        linea_puntos_1_2.start_point = coord_punto_1
        linea_puntos_1_2.end_point = coord_punto_2
        coord_punto_3 = skecth_open_edition.create_point(x1+long_lado_h, y1)  #(point2D3 -> coord_punto_3)
        coord_punto_3.report_name = 6
        coord_punto_3.name = "Coordenadas punto 3"
        linea_puntos_2_3 = skecth_open_edition.create_line(x1+long_lado_h, y1+long_lado_v, x1+long_lado_h, y1)  #(line2D4 -> linea_puntos_2_3)
        linea_puntos_2_3.report_name = 7
        linea_puntos_2_3.name = "Linea union puntos 2-3"
        linea_puntos_2_3.end_point = coord_punto_2
        linea_puntos_2_3.start_point = coord_punto_3
        coord_punto_4 = skecth_open_edition.create_point(x1, y1)  #(point2D4 -> coord_punto_4)
        coord_punto_4.report_name = 8
        coord_punto_4.name = "Coordenadas punto 4"
        linea_puntos_3_4 = skecth_open_edition.create_line(x1+long_lado_h, y1, x1, y1)  #(line2D5 -> linea_puntos_3_4)
        linea_puntos_3_4.report_name = 9
        linea_puntos_3_4.name = "Linea union puntos 3-4"
        linea_puntos_3_4.start_point = coord_punto_3
        linea_puntos_3_4.end_point = coord_punto_4
        linea_puntos_4_1 = skecth_open_edition.create_line(x1, y1, x1, y1+long_lado_v) #(line2D6 -> linea_puntos_4_1)
        linea_puntos_4_1.report_name = 10
        linea_puntos_4_1.name = "Linea union punto 4-1"
        linea_puntos_4_1.end_point = coord_punto_4
        linea_puntos_4_1.start_point = coord_punto_1

        #CREA CONSTRAINTS
        create_constraint = sketch.constraints  #(constraints1 -> create_constraint)
        reference2 = part.create_reference_from_object(linea_puntos_1_2) #(para entender cual es la referencia solo te tienes que fijar en el objeto: renference2 = linea_puntos_1_2)
        reference3 = part.create_reference_from_object(h_axis)
        cst1_paralelismo = create_constraint.add_bi_elt_cst(cat_constraint_type.index("catCstTypeHorizontality"), reference2, reference3)  #(constraint1 -> cst1_paralelismo)
        cst1_paralelismo.mode = cat_constraint_mode.index("catCstModeDrivingDimension")
        cst1_paralelismo.name = "Paralelismo"
        reference4 = part.create_reference_from_object(linea_puntos_3_4)
        reference5 = part.create_reference_from_object(h_axis)
        cst2_paralelismo = create_constraint.add_bi_elt_cst(cat_constraint_type.index("catCstTypeHorizontality"), reference4, reference5)
        cst2_paralelismo.mode = cat_constraint_mode.index("catCstModeDrivingDimension")
        cst2_paralelismo.name = "Paralelismo"
        reference6 = part.create_reference_from_object(linea_puntos_2_3)
        reference7 = part.create_reference_from_object(v_axis)
        cst3_paralelismo = create_constraint.add_bi_elt_cst(cat_constraint_type.index("catCstTypeVerticality"), reference6, reference7)
        cst3_paralelismo.mode = cat_constraint_mode.index("catCstModeDrivingDimension")
        cst3_paralelismo.name = "Paralelismo"
        reference8 = part.create_reference_from_object(linea_puntos_4_1)
        reference9 = part.create_reference_from_object(v_axis)
        cst4_paralelismo = create_constraint.add_bi_elt_cst(cat_constraint_type.index("catCstTypeVerticality"), reference8, reference9)
        cst4_paralelismo.mode = cat_constraint_mode.index("catCstModeDrivingDimension")
        cst4_paralelismo.name = "Paralelismo"
        reference10 = part.create_reference_from_object(linea_puntos_2_3)
        cst5_dimension = create_constraint.add_mono_elt_cst(cat_constraint_type.index("catCstTypeLength"), reference10)
        cst5_dimension.mode = cat_constraint_mode.index("catCstModeDrivingDimension")
        longitud_lado_v = cst5_dimension.dimension
        longitud_lado_v.value = long_lado_v
        cst5_dimension.name = "Longitud lado V"
        reference11 = part.create_reference_from_object(linea_puntos_3_4)
        cst6_dimension = create_constraint.add_mono_elt_cst(cat_constraint_type.index("catCstTypeLength"), reference11)
        cst6_dimension.mode = cat_constraint_mode.index("catCstModeDrivingDimension")
        longitud_lado_h = cst6_dimension.dimension
        longitud_lado_h.value = long_lado_h
        cst6_dimension.name = "Longitud lado H"
        reference12 = part.create_reference_from_object(coord_punto_4)
        reference13 = part.create_reference_from_object(h_axis)
        cst7_offset_h = create_constraint.add_bi_elt_cst(cat_constraint_type.index("catCstTypeDistance"), reference12, reference13)
        cst7_offset_h.mode = cat_constraint_mode.index("catCstModeDrivingDimension")
        long_offset_h = cst7_offset_h.dimension
        long_offset_h.value = y1
        cst7_offset_h.name = "Offset_h_punto_4"
        reference14 = part.create_reference_from_object(coord_punto_4)
        reference15 = part.create_reference_from_object(v_axis)
        cst8_offset_v = create_constraint.add_bi_elt_cst(cat_constraint_type.index("catCstTypeDistance"), reference14, reference15)
        cst8_offset_v.mode = cat_constraint_mode.index("catCstModeDrivingDimension")
        long_offset_v = cst8_offset_v.dimension
        long_offset_v.value = x1
        cst8_offset_v.name ="Offset_v_punto_4"
        sketch.close_edition 
        part.in_work_object = body
        part.update_object(sketch)
        part.in_work_object = body
        shapeFactory1 = part.shape_factory

        #CREA PAD
        pad = shapeFactory1.add_new_pad(sketch, l_pad)
        pad.name = ("Pad: "+ data_new[i]["name"])
        part.update_object(pad)

    document.save_as(rutas_CARGAS + "\Cargapago.CATPart", overwrite = True)
    document.close()

    return numero_cargas_pago_new