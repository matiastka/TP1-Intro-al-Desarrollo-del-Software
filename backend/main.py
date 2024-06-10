#Acá va a estar los endpoints de la página (usando flask y flask cors)
from flask import Flask, jsonify, request

#from flask_cors import CORS #importamos CORS para que ande el fetch entre 2 páginas

from models import db, Vendedores, Autos

app = Flask(__name__) #denominamos a flask
port = 5000

#CORS(app) #Con esto van a andar los fetch entre 2 páginas distintas (o una página externa)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://atufullana:misticaroja2011@localhost:5432/db_tp1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route("/") #Si solicitan la homepage del servidor
def home():
    return "hola mundo"

@app.route("/autos/<id_auto>") #pagina de un auto con cierto id
def auto(id_auto):
    try:
        auto = Autos.query.get(id_auto)
        auto_data = {
            'id': auto.id, 
            'nombre': auto.nombre_auto, 
            'marca': auto.marca, 
            'color': auto.color, 
            'cantidad de asientos': auto.cant_asientos, 
            'tipo de baul': auto.tipo_baul, 
            '¿caja automatica?': auto.caja_automatica, 
            '¿caja manual?': auto.caja_manual, 
            'precio': auto.precio, 
            'kilometros': auto.kilometros, 
            'ubicacion': auto.ubicacion, 
            'Vendedor': auto.author_id
            }
        return jsonify(auto_data)
    except: 
        return jsonify({"mensaje":"que haces acá, sacá la mano de ahí carajo"})

if __name__ == '__main__':
    print('Iniciando servidor...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('Servidor Cerrado...')