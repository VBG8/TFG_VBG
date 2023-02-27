#Renovación del archivo JSON

def Renovar_json(move, remove, data_new, rutas_JSON):

    remove (rutas_JSON + "\datos_viejos.json")

    import json
    with open (rutas_JSON + '\datos_nuevos.json', "w") as componente:
        data_nuevos = json.dump(data_new, componente)

    move (rutas_JSON + "\datos_nuevos.json", rutas_JSON + "\datos_viejos.json")