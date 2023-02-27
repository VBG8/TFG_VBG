##VISUALIZACION DE LAS CARGAS DE PAGO DENTRO DEL DRON Y CREACION DE STLs

def Creacion_de_STLs(catia, cat_constraint_type, cat_constraint_orientation, rutas_CARGAS, ruta_CDG_cargado, ruta_STLs):
    caa = catia()
    caa.display_file_alerts = False
    documents = caa.documents
    #documents.open(r"C:\CATIA\Diseño Dron\Ensamble definitivo dron\Ensamblaje del dron.CATProduct")
    document = caa.active_document
    product = document.product
    sub_products = product.products

    #Ensamblo las cargas de pago en el dron y creo constraints

    sub_products.add_components_from_files([rutas_CARGAS + "\Cargapago.CATPart"], "CATPart")

    product = product.reference_product

    create_constraint_1 = product.constraints()
    reference_angle_xy_fus = product.create_reference_from_name("Emsamblaje del dron/Fuselaje/!xy plane")
    reference_angle_xy_CP = product.create_reference_from_name("Emsamblaje del dron/Part1.1/!xy plane")
    constraint_angle_1 = create_constraint_1.add_bi_elt_cst(cat_constraint_type.index("catCstTypeAngle"), reference_angle_xy_fus, reference_angle_xy_CP)
    angle1 = constraint_angle_1.dimension
    angle1.value = 180
    cat_cst_angle_sector = 0
    constraint_angle_1.angle_sector = cat_cst_angle_sector 

    create_constraint_2 = product.constraints()
    reference_angle_zx_fus = product.create_reference_from_name("Emsamblaje del dron/Fuselaje/!zx plane")
    reference_angle_zx_CP = product.create_reference_from_name("Emsamblaje del dron/Part1.1/!zx plane")
    constraint_angle_2 = create_constraint_2.add_bi_elt_cst(cat_constraint_type.index("catCstTypeAngle"), reference_angle_zx_fus, reference_angle_zx_CP)
    angle2 = constraint_angle_2.dimension
    angle2.value = 180
    cat_cst_angle_sector = 0
    constraint_angle_2.angle_sector = cat_cst_angle_sector 

    create_constraint3 = product.constraints()
    reference_CP_xy= product.create_reference_from_name("Emsamblaje del dron/Part1.1/!xy plane")
    reference_fus_suelo = product.create_reference_from_name("Emsamblaje del dron/Fuselaje/!Selection_RSur:(Face:(Brp:((Brp:(Pocket.15;0:(Brp:(Sketch.65;1)));Brp:(Pocket.9;2)));None:();Cf11:());Pad.12_ResultOUT;Z0;G4074)")
    constraint_offset1 = create_constraint3.add_bi_elt_cst(cat_constraint_type.index("catCstTypeDistance"), reference_CP_xy, reference_fus_suelo)
    length1 = constraint_offset1.dimension
    length1.value = 0.000000
    constraint_offset1.orientation = cat_constraint_orientation.index("catCstOrientSame")

    create_constraint4 = product.constraints()
    reference_CP_zx = product.create_reference_from_name("Emsamblaje del dron/Part1.1/!zx plane")
    reference_fus_zx = product.create_reference_from_name("Emsamblaje del dron/Fuselaje/!zx plane")
    constraint_offset2 = create_constraint4.add_bi_elt_cst(cat_constraint_type.index("catCstTypeDistance"), reference_CP_zx, reference_fus_zx)
    length2 = constraint_offset2.dimension
    length2.value = 0.000000
    constraint_offset2.orientation = cat_constraint_orientation.index("catCstOrientOpposite")

    create_constraint5 = product.constraints()
    reference_CP_yz = product.create_reference_from_name("Emsamblaje del dron/Part1.1/!yz plane")
    reference_lado_dron = product.create_reference_from_name("Emsamblaje del dron/Fuselaje/!Selection_RSur:(Face:(Brp:(Pocket.9;0:(Brp:(GSMTranslate.1;(Brp:(GSMRotate.1;(Brp:(Sketch.6;35)))))));AtLeastOneNoSharedIncluded:(Brp:(Pad.12;2);Brp:(Pocket.26;0:(Brp:(Sketch.84;2)));Brp:(Pocket.15;0:(Brp:(Sketch.65;2))));Cf11:());Pad.12_ResultOUT;Z0;G4074)")
    constraint_offset3 = create_constraint5.add_bi_elt_cst(cat_constraint_type.index("catCstTypeDistance"), reference_CP_yz, reference_lado_dron)
    length3 = constraint_offset3.dimension
    length3.value = 0.000000
    constraint_offset3.orientation = cat_constraint_orientation.index("catCstOrientSame")

    product.update ()  

    #Ensamblo el CDG y creo constraints

    sub_products.add_components_from_files([ruta_CDG_cargado + "\CuboCDG_Cargado.CATPart"], "CATPart")

    #Constraints para posicionar el CDG en el dron

    product = product.reference_product

    create_constraint_6 = product.constraints()
    reference_angle_zx_fus_2 = product.create_reference_from_name("Emsamblaje del dron/Fuselaje/!zx plane")
    reference_angle_zx_CDG = product.create_reference_from_name("Emsamblaje del dron/Part1.2/!zx plane")
    constraint_angle_3 = create_constraint_6.add_bi_elt_cst(cat_constraint_type.index("catCstTypeAngle"), reference_angle_zx_fus_2, reference_angle_zx_CDG)
    angle3 = constraint_angle_3.dimension
    angle3.value = 180
    cat_cst_angle_sector = 0
    constraint_angle_3.angle_sector = cat_cst_angle_sector

    create_constraint_7 = product.constraints()
    reference_angle_yz_fus_2 = product.create_reference_from_name("Emsamblaje del dron/Fuselaje/!yz plane")
    reference_angle_yz_CDG = product.create_reference_from_name("Emsamblaje del dron/Part1.2/!yz plane")
    constraint_angle_4 = create_constraint_6.add_bi_elt_cst(cat_constraint_type.index("catCstTypeAngle"), reference_angle_yz_fus_2, reference_angle_yz_CDG)
    angle4 = constraint_angle_4.dimension
    angle4.value = 0
    cat_cst_angle_sector = 0
    constraint_angle_4.angle_sector = cat_cst_angle_sector

    product.update()

    ##Esconde todos los subproducts menos el de la carga de pago o el CDG para generar posteriormente el STL de cada uno de ellos

    for i in sub_products:
        selection = document.selection
        selection.clear()
        selection.add(i)
        selection.vis_properties.set_show(1)

    selection.clear()

    selectionCP = document.selection
    selectionCP.add(sub_products[41])
    selectionCP.vis_properties.set_show(0)
    document = product.generate_ALLCATPart(sub_products[41]) #Genera el CATPART solo de las CARGAS DE PAGO con unos ejes de referencia globales, iguales a los ejes del resto de piezas del dron cargadas en la pagina HTML
    document.export_data(ruta_STLs + "\Parte_CargaPago.stl", "stl", overwrite = True)
    document.close()

    #Limpio y borro la seleccion de la carga de pago
    document = caa.active_document
    selectionCP_delete = document.selection
    selectionCP_delete.add(sub_products[41])
    selectionCP_delete.delete()
    #Genero CATPart del cuboCDG
    selectionCDG = document.selection
    selectionCDG.add(sub_products[41])
    selectionCDG.vis_properties.set_show(0)
    document = product.generate_ALLCATPart(sub_products[41])
    document.export_data(ruta_STLs + "\Parte_CuboCDG_CARGADO.stl", "stl", overwrite = True)
    document.close()
    #Limpio y borro la seleccion para volver a mostrar todos los elementos con normalidad y a continuacion cierro CATIA
    document = caa.active_document
    selectionCDG_delete = document.selection
    selectionCDG_delete.add(sub_products[41])  #Vuelvo a poner 41 porque aunque sea 42, al borrar el 41 (CARGA DE PAGO), el 42 pasa ahora a ser 41
    selectionCDG_delete.delete()
    selection.clear()
    for i in sub_products:
        selection = document.selection
        selection.clear()
        selection.add(i)
        selection.vis_properties.set_show(0)
    selection.clear()
    document.close()