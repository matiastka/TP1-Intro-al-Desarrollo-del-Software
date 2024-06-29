#Acá va a estar los endpoints de la página (usando flask y flask cors)
from flask import Flask, jsonify, request
from flask_cors import CORS #importamos CORS para que ande el fetch entre 2 páginas

from models import db, Vendedores, Autos, Compradores

app = Flask(__name__) #denominamos a flask
CORS(app) #Con esto van a andar los fetch entre 2 páginas distintas (o una página externa)
port = 5000

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://matiastka:kini9853@localhost:5432/db_tp1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route("/") #Si solicitan la homepage del servidor
def home():
    return "hola mundo"

@app.route("/autos/<id_auto>") #Endpoint que muestra auto por cierto id
def mostrar_auto(id_auto):
    try:
        auto = Autos.query.get(id_auto)
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
            'link': auto.link,
            'vendedor_id': auto.vendedor_id
            }
        return jsonify(auto_data)
    except: 
        return jsonify({"mensaje":"El auto que buscaste no existe"})

@app.route("/autos/")  #Endpoint que muestra todos los autos
def mostrar_autos():
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
                'link': auto.link,
                'vendedor_id': auto.vendedor_id
                }
            autos_data.append(auto_data)
        if (len(autos_data) == 0):
            return jsonify({'mensaje': 'No hay autos'})
        return jsonify(autos_data)
    except:
        return jsonify({
            'mensaje': 'Error interno del server'
        })

@app.route('/autos/', methods=['POST'])
def agregar_auto(): #endpoint para agregar un auto
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
        nuevo_link = data.get('link')
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
            link=nuevo_link,
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
            'link': nuevo_link,
            'vendedor_id': nuevo_auto.vendedor_id}, 'Success': True
            }
            ), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'mensaje': 'Error interno del server'}), 500

@app.route('/autos/<id_auto>', methods=['DELETE']) #endpoint para eliminar un auto por cierto id
def eliminar_auto(id_auto):
    try:
        Autos.query.filter(Autos.id == int(id_auto)).delete() #Elimina
        db.session.commit() #Confirmamos en la base de datos el delete
        return jsonify({'Success': True})
    except:
        return jsonify({'mensaje': 'No existe al auto a borrar'})

@app.route('/autos/<id_auto>', methods=['PUT']) #endpoint para editar un auto por cierto id (pensar como hacer para que sea igual al endpoint de crear autos)
def editar_auto(id_auto):
    try:
        data = request.json #Obtiene el contenido del body (por ser metodo POST)
        auto_a_editar = Autos.query.get(id_auto)

        auto_a_editar.nombre_auto = data.get('nombre_auto')
        auto_a_editar.marca = data.get('marca')
        auto_a_editar.color = data.get('color')
        auto_a_editar.cant_asientos = data.get('cant_asientos')
        auto_a_editar.tipo_baul = data.get('tipo_baul')
        auto_a_editar.caja_automatica = data.get('caja_automatica')
        auto_a_editar.caja_manual = data.get('caja_manual')
        auto_a_editar.precio = data.get('precio')
        auto_a_editar.kilometros = data.get('kilometros')
        auto_a_editar.ubicacion = data.get('ubicacion')
        auto_a_editar.anio = data.get('anio')
        auto_a_editar.link = data.get('link')
        #auto_a_editar.vendedor_id = data.get('vendedor_id')
        db.session.commit()

        return jsonify({'Success': True}), 200
    except Exception as error:
        print('Error', error)
        return jsonify({'mensaje': 'Error al editar el auto'}), 500

@app.route('/vendedores/<id_vendedor>') #Endpoint para mostrar un vendedor
def mostrar_vendedor(id_vendedor):
    try:
        vendedor = Vendedores.query.get(id_vendedor)
        vendedor_data = {
            'id': vendedor.id, 
            'nombre_vendedor': vendedor.nombre_vendedor, 
            }
        return jsonify(vendedor_data)
    except: 
        return jsonify({"mensaje":"El vendedor que buscaste no existe"})

@app.route('/vendedores') #Endpoint para mostrar todos los vendedores
def mostrar_vendedores():
    try:
        vendedores = Vendedores.query.all()
        vendedores_data = []
        for vendedor in vendedores:
            vendedor_data = {
                'id': vendedor.id,
                'nombre_vendedor': vendedor.nombre_vendedor
            }
            vendedores_data.append(vendedor_data) #Sino va a dentro del for solo apeendea el último.
        if (len(vendedor_data) == 0):
            return jsonify({"mensaje": 'No hay vendedores'})
        return jsonify(vendedores_data)
    except:
        return jsonify({'mensaje': 'Error interno del server'}), 500

@app.route('/vendedores', methods=['POST']) #Endpoint para crear un vendedor
def agregar_vendedor():
    try:
        data = request.json #Obtiene el contenido del body (por ser metodo POST)
        nuevo_nombre = data.get('nombre_vendedor') #Obtiene el valor de la columna nombre_comprador
        #lista_vendedores = Vendedores.query.all()  Forma vieja de conseguir el id del vendedor (en simultaneo con el frontend)
        #id = len(lista_vendedores) + 1 #Obtenemos el id, contando el largo de la lista (que la lista son los vendedores) le sumamos uno.
        nuevo_vendedor = Vendedores(
            nombre_vendedor=nuevo_nombre
            )
        db.session.add(nuevo_vendedor)
        db.session.commit()
        return jsonify({'vendedores': {
            'id': nuevo_vendedor.id, 
            'nombre_vendedor': nuevo_vendedor.nombre_vendedor},'Success': True
            }
            ), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'mensaje': 'Error interno del server'}), 500

@app.route('/vendedores/<id_vendedor>', methods=['PUT']) #Endpoint para editar un vendedor
def editar_vendedor(id_vendedor):
    try:
        data = request.json #Obtiene el contenido del body (por ser metodo POST)
        vendedor_a_editar = Vendedores.query.get(id_vendedor)

        vendedor_a_editar.nombre_vendedor = data.get('nombre_vendedor')
        db.session.commit()

        return jsonify({'Success': True}), 200
    except Exception as error:
        print('Error', error)
        return jsonify({'mensaje': 'Error al editar el vendedor'}), 500

@app.route('/compradores/<id_comprador>') #Endpoint para mostrar un comprador
def mostrar_comprador(id_comprador):
    try:
        comprador = Compradores.query.get(id_comprador)
        comprador_data = {
            'id': comprador.id, 
            'nombre_comprador': comprador.nombre_comprador, 
            'plata': comprador.plata
            }
        return jsonify(comprador_data)
    except: 
        return jsonify({"mensaje":"El comprador que buscaste no existe"})

@app.route('/compradores/<id_comprador>', methods=['PUT']) #Endpoint para editar el perfil de un comprador
def editar_comprador(id_comprador):
    try:
        data = request.json #Obtiene el contenido del body (por ser metodo POST)
        comprador_a_editar = Compradores.query.get(id_comprador)

        comprador_a_editar.nombre_comprador = data.get('nombre_comprador')
        db.session.commit()

        return jsonify({'Success': True}), 200
    except Exception as error:
        print('Error', error)
        return jsonify({'mensaje': 'Error al editar el comprador'}), 500

@app.route('/compradores', methods=['POST'])
def agregar_comprador():
    try:
        data = request.json #Obtiene el contenido del body (por ser metodo POST)
        nuevo_nombre = data.get('nombre_comprador') #Obtiene el valor de la columna nombre_comprador
        nueva_plata = data.get('plata')
        nuevo_comprador = Compradores(
            nombre_comprador=nuevo_nombre,
            plata=nueva_plata
            )
        db.session.add(nuevo_comprador)
        db.session.commit()
        return jsonify({'compradores': {
            'id': nuevo_comprador.id, 
            'nombre_comprador': nuevo_comprador.nombre_comprador, 
            'plata': nuevo_comprador.plata}, 'Success': True
            }
            ), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'mensaje': 'Error interno del server'}), 500

if __name__ == 'main':
    print('Iniciando servidor...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('Servidor Cerrado...')