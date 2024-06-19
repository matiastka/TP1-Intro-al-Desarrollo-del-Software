#Acá tenemos la relación entre nuestra de BD y Backend
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vendedores(db.Model):
    __tablename__ = 'vendedores'
    id = db.Column(db.Integer, primary_key=True)
    nombre_vendedor = db.Column(db.String(255), nullable=False)
    
class Autos(db.Model):
    __tablename__ = 'autos'
    id = db.Column(db.Integer, primary_key=True)
    nombre_auto = db.Column(db.String(255), nullable=False)
    marca = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(255), nullable=False)
    cant_asientos = db.Column(db.Integer, nullable=False)
    tipo_baul = db.Column(db.String(255), nullable=False)
    caja_automatica = db.Column(db.Boolean , default=False)
    caja_manual = db.Column(db.Boolean , default=False)
    precio = db.Column(db.Integer, nullable=False)
    kilometros = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    link = db.Column(db.String(255), nullable=False)
    vendedor_id = db.Column(db.Integer, db.ForeignKey('vendedores.id'))

class Compradores(db.Model):
    __tablename__ = 'compradores'
    id = db.Column(db.Integer, primary_key=True)
    nombre_comprador = db.Column(db.String(255), nullable=False)
    plata = db.Column(db.Integer, default=0)
