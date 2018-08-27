# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Usuario(Base):
    __tablename__ = 'Usuario'

    Id_Usuario = Column(Integer, primary_key=True)
    Email = Column(String(100, 'Modern_Spanish_CI_AS'))
    Clave = Column(String(50, 'Modern_Spanish_CI_AS'))
