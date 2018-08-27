'''
from PropiedadesApp.models.usuario import Usuario
from sqlalchemy.orm import sessionmaker
#from django.conf import settings


engine =  usuario.db_connect
usuario.create_deals_table()

Session = sessionmaker(bind=engine)
'''





