#Borra los prismas antiguos de Catia, siempre que haya algo que borrar
# 
def borrar_cargas(data_viejos, numero_cargas_pago_old, catia, rutas_CARGAS):
    if numero_cargas_pago_old != 1:
        ##Abre catia para borrar elementos
        caa = catia()
        documents = caa.documents
        documents.open(rutas_CARGAS + "\Cargapago.CATPart")
        document = caa.active_document
        part = document.part

        ##Borrar elementos
        bodies1 = part.bodies
        body1 = bodies1.get_item("Carga de pago")
        sketches1 = body1.sketches
        shapes1 = body1.shapes
        hybridBodies1 = part.hybrid_bodies
        selection = document.selection
        selection.clear

        for i in range(1, numero_cargas_pago_old):
            pad = shapes1.get_item("Pad: "+ data_viejos[i]["name"])
            sketch = sketches1.get_item("Sketch: "+ data_viejos[i]["name"])
            geom_set = hybridBodies1.get_item("Construction Geometry: "+ data_viejos[i]["name"])
            hybridShapes1 = geom_set.hybrid_shapes
            hsp = hybridShapes1.get_item("Plane Offset: "+ data_viejos[i]["name"])
            selection.add(pad)
            selection.add(sketch)
            selection.add(hsp)
            selection.add(geom_set)
            selection.delete()

        document.save_as(rutas_CARGAS + "\Cargapago.CATPart", overwrite = True)
        document.close()