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
            'anio': auto.anio,
            'Vendedor': auto.vendedor_id
            }
        return jsonify(auto_data)
    except: 
        return jsonify({"mensaje":"El vendedor que buscaste no existe"})

@app.route("/autos/")  #Página de los autos
def autos():
    try:  
        autos = Autos.query.all()
        autos_data = []
        for auto in autos:
            auto_data = {
                'id': auto.id,
                'nombre_auto': auto.nombre_auto,
                'marca': auto.marca,
                'color': auto.color,
                'cant_asientos': auto.cant_asientos,
                'tipo_baul': auto.tipo_baul,
                'caja_automatica': auto.caja_automatica,
                'caja_manual': auto.caja_manual,
                'precio': auto.precio,
                'kilometros': auto.kilometros,
                'ubicacion': auto.ubicacion,
                'anio': auto.anio,
                'vendedor_id': auto.vendedor_id
                }
            autos_data.append(auto_data)
        return jsonify(autos_data)
    except:
        return jsonify({
            'mensaje': 'No hay autos'
        })

@app.route('/autos', methods=['POST'])
def agregar_auto():
    try:
        data = request.json #Obtiene el contenido del body (por ser metodo POST)
        nuevo_nombre = data.get('nombre_auto') #Obtiene el valor de la columna nombre_auto
        nueva_marca = data.get('marca')
        nuevo_color = data.get('color')
        nueva_cant_asientos = data.get('cant_asientos')
        nuevo_tipo_baul = data.get('tipo_baul')
        nueva_caja_automatica = data.get('caja_automatica')
        nueva_caja_manual = data.get('caja_manual')
        nuevo_precio = data.get('precio')
        nuevo_kilometros = data.get('kilometros')
        nueva_ubicacion = data.get('ubicacion')
        nuevo_anio = data.get('anio')
        nuevo_vendedor_id = data.get('vendedor_id')
        nuevo_auto = Autos(
            nombre_auto=nuevo_nombre, #El nombre de la variable tiene que ser igual al de las columnas
            marca=nueva_marca, 
            color=nuevo_color, 
            cant_asientos=nueva_cant_asientos, 
            tipo_baul=nuevo_tipo_baul, 
            caja_automatica=nueva_caja_automatica, 
            caja_manual=nueva_caja_manual,
            precio=nuevo_precio,
            kilometros=nuevo_kilometros,
            ubicacion=nueva_ubicacion,
            anio=nuevo_anio,
            vendedor_id=nuevo_vendedor_id
            )
        db.session.add(nuevo_auto)
        db.session.commit()
        return jsonify({'autos': {
            'id': nuevo_auto.id, 
            'nombre_auto': nuevo_auto.nombre_auto, 
            'marca': nuevo_auto.marca, 
            'color': nuevo_auto.color,
            'cant_asientos': nuevo_auto.cant_asientos,
            'tipo_baul': nuevo_auto.tipo_baul,
            'caja_automatica': nuevo_auto.caja_automatica,
            'caja_manual': nuevo_auto.caja_manual,
            'precio': nuevo_auto.precio,
            'kilometros': nuevo_auto.kilometros,
            'ubicacion': nuevo_auto.ubicacion,
            'anio': nuevo_auto.anio,
            'vendedor_id': nuevo_auto.vendedor_id}
            }
            ), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'mensaje': 'Error interno del server'}), 500

@app.route("/autos/<id_auto>/<id_vendedor>") #pagina de un vendedor con cierto id
def vendedor(id_auto,id_vendedor):
    try:
        vendedor = Vendedores.query.get(id_vendedor)
        vendedor_data = {
            'id': vendedor.id, 
            'nombre': vendedor.nombre_vendedor, 
            }
        return jsonify(vendedor_data)
    except: 
        return jsonify({"mensaje":"El vendedor que buscaste no existe"})

if __name__ == '__main__':
    print('Iniciando servidor...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('Servidor Cerrado...')