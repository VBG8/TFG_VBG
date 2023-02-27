from flask import Flask, request, jsonify, json
from flask_cors import CORS
from CDG_CP_pycatia_FUNCION import Calculo_cdg, Calcular_AyA

#Set up Flask:
app = Flask(__name__)
#Set up Flask to bypass CORS at the front end:
cors = CORS(app)

@app.route("/datos_cargas/<myjson>")
def postME1(myjson):
   datos = json.loads(myjson)
   resultado = Calculo_cdg(datos)
   resultado = jsonify(resultado)
   return resultado

@app.route("/datos_AyA/<ourjson>")
def postME2(ourjson):
   datos_AyA = json.loads(ourjson)
   resultado_AyA = Calcular_AyA(datos_AyA)
   resultado_AyA = jsonify(resultado_AyA)
   return resultado_AyA

#Run the app:
if __name__ == "__main__":
     app.run(debug=True)