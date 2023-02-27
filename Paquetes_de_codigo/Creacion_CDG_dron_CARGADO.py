##Codigo que crea el cubo que muestra el CDG del DRON CARGADO

def Crear_CDG_dron_CARGADO(catia, x_cdg_total, y_cdg_total, z_cdg_total, cat_constraint_type, cat_constraint_mode, ruta_CDG_cargado):
    #Activa Catia y borra el CDG que exista
    caa = catia()
    caa.display_file_alerts = False
    documents = caa.documents
    documents.open(ruta_CDG_cargado + "\CuboCDG_Cargado.CATPart")
    document = caa.active_document
    part = document.part

    bodies = part.bodies
    body = bodies.get_item("Cubo CDG DRON CARGADO")
    sketch = body.sketches
    shapes = body.shapes
    hbs = part.hybrid_bodies
    selection = document.selection
    selection.clear()
    pad = shapes.get_item("Pad: Cubo CDG DRON CARGADO")
    sketch = sketch.get_item("Sketch: Cubo CDG DRON CARGADO")
    geom_set = hbs.get_item("Construction Geometry: Cubo CDG DRON CARGADO")
    hybrid_shapes = geom_set.hybrid_shapes
    hsp = hybrid_shapes.get_item("Plane Offset: Cubo CDG DRON CARGADO")
    selection.add(pad)
    selection.add(sketch)
    selection.add(hsp)
    selection.add(geom_set)
    selection.delete()
    document.save_as(ruta_CDG_cargado + "\CuboCDG_Cargado.CATPart", overwrite = True)
    document.close()

    ##Creacion nuevo CDG
    caa = catia()
    caa.display_file_alerts = False
    documents = caa.documents
    documents.open(ruta_CDG_cargado + "\CuboCDG_Cargado.CATPart")
    document = caa.active_document
    part = document.part
    body = part.main_body
    body.name = "Cubo CDG DRON CARGADO"


    x1 = (x_cdg_total)
    y1 = (y_cdg_total)
    h_off = (z_cdg_total)
    l_pad = 10
    long_lado_h = 10
    long_lado_v = 10

    sketches = body.sketches
    hbs = part.hybrid_bodies
    geom_set = hbs.add()
    geom_set.name = ("Construction Geometry: Cubo CDG DRON CARGADO")
    originElements = part.origin_elements
    hsf = part.hybrid_shape_factory
    hsp = originElements.plane_xy  
    reference = part.create_reference_from_object(hsp)
    hsp_plane_offset = hsf.add_new_plane_offset(reference, h_off, False)  
    geom_set.append_hybrid_shape(hsp_plane_offset)
    hsp_plane_offset.name = ("Plane Offset: Cubo CDG DRON CARGADO")
    part.in_work_object = hsp_plane_offset
    part.update()
    sketch = sketches.add(hsp_plane_offset)
    sketch.name = ("Sketch: Cubo CDG DRON CARGADO")
    part.in_work_object = sketch
    skecth_open_edition = sketch.open_edition()
    geometricElements = sketch.geometric_elements
    absolute_axis = geometricElements.item("AbsoluteAxis")
    h_axis = absolute_axis.get_item("HDirection")
    h_axis.report_name = 1
    v_axis = absolute_axis.get_item("VDirection")
    v_axis.report_name = 2

    #Creacion del cubito
    coord_punto_1 = skecth_open_edition.create_point(x1, y1+long_lado_v) 
    coord_punto_1.report_name = 3
    coord_punto_1.name = "Coordenadas punto 1"
    coord_punto_2 = skecth_open_edition.create_point(x1+long_lado_h, y1+long_lado_v)  
    coord_punto_2.report_name = 4
    coord_punto_2.name = "Coordenadas punto 2"
    linea_puntos_1_2 = skecth_open_edition.create_line(x1, y1+long_lado_v, x1+long_lado_h, y1+long_lado_v) 
    linea_puntos_1_2.report_name = 5
    linea_puntos_1_2.name = "Linea union puntos 1-2"
    linea_puntos_1_2.start_point = coord_punto_1
    linea_puntos_1_2.end_point = coord_punto_2
    coord_punto_3 = skecth_open_edition.create_point(x1+long_lado_h, y1)  
    coord_punto_3.report_name = 6
    coord_punto_3.name = "Coordenadas punto 3"
    linea_puntos_2_3 = skecth_open_edition.create_line(x1+long_lado_h, y1+long_lado_v, x1+long_lado_h, y1)  
    linea_puntos_2_3.report_name = 7
    linea_puntos_2_3.name = "Linea union puntos 2-3"
    linea_puntos_2_3.end_point = coord_punto_2
    linea_puntos_2_3.start_point = coord_punto_3
    coord_punto_4 = skecth_open_edition.create_point(x1, y1)  
    coord_punto_4.report_name = 8
    coord_punto_4.name = "Coordenadas punto 4"
    linea_puntos_3_4 = skecth_open_edition.create_line(x1+long_lado_h, y1, x1, y1)  
    linea_puntos_3_4.report_name = 9
    linea_puntos_3_4.name = "Linea union puntos 3-4"
    linea_puntos_3_4.start_point = coord_punto_3
    linea_puntos_3_4.end_point = coord_punto_4
    linea_puntos_4_1 = skecth_open_edition.create_line(x1, y1, x1, y1+long_lado_v) 
    linea_puntos_4_1.report_name = 10
    linea_puntos_4_1.name = "Linea union punto 4-1"
    linea_puntos_4_1.end_point = coord_punto_4
    linea_puntos_4_1.start_point = coord_punto_1

    #Creacion de constraints
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
    shapeFactory = part.shape_factory

    #CREA PAD
    pad = shapeFactory.add_new_pad(sketch, l_pad)
    pad.name = ("Pad: Cubo CDG DRON CARGADO")
    part.update_object(pad)

    part.update()
    document.save_as(ruta_CDG_cargado + "\CuboCDG_Cargado.CATPart", overwrite = True)
    document.close()