#Acá tenemos la relación entre nuestra de BD y Backend
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Autos(db.Model): #se encarga Atu
    __tablename__ = 'autos'
    id = db.Column(db.Integer, primary_key=True)
    nombre_auto = db.Column(db.String(255), nullable=False)
    marca = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(255), nullable=False)
    cant_asientos = db.Column(db.Integer, nullable=False)
    tipo_baul = db.Column(db.String(255), nullable=False)
    caja_automatica = db.Column(db.Boolean , nullable=False)
    caja_manual = db.Column(db.Boolean , nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    kilometros = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('vendedores.id'))