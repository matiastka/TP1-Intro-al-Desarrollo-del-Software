#Acá va a estar los endpoints de la página (usando flask y flask cors)
from flask import Flask
#from models import db

#from flask_cors import CORS #importamos CORS para que ande el fetch entre 2 páginas

app = Flask(__name__) #denominamos a flask
port = 5000

#CORS(app) #Con esto van a andar los fetch entre 2 páginas distintas (o una página externa)

@app.route("/") #Si solicitan la homepage del servidor
def home():
    return "hola mundo"

