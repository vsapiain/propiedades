# coding: utf-8
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from PropiedadesApp.models.db import metadata

#Base = declarative_base()
#metadata = Base.metadata

class Usuario(metadata):
    __tablename__ = 'Usuario'

    Id_Usuario = Column(Integer, primary_key=True)
    Email = Column(String(100, 'Modern_Spanish_CI_AS'))
    Clave = Column(String(50, 'Modern_Spanish_CI_AS'))


