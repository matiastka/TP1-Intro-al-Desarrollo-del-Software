#Acá tenemos la relación entre nuestra de BD y Backend
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vendedores(db.Model):
    __tablename__ = 'vendedores'
    id = db.Column(db.Integer, primary_key=True)
    nombre_de_usuario = db.Column(db.String(255), nullable=False)