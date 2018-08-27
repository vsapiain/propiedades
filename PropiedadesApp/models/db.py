# coding: utf-8
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.exc import DatabaseError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker

db_engine = 'mssql+pymssql://sa:admin.2013@186.64.123.187/citypro'
engine = create_engine(db_engine)
session = scoped_session(sessionmaker(autocommit=False, bind=engine))

class db_base:
    def save(self):
        session.add(self)
        self._flush()
        session.commit()
        session.refresh(self)
        return self

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save()

    def get(self,id):
        return self.query.get(id)

    def delete(self):
        session.delete(self)
        self._commit()
        session.close()

    def _commit(self):
        try:
            session.commit()
        except DatabaseError:
            session.rollback()
            raise

    def _flush(self):
        try:
            session.flush()
        except DatabaseError:
            session.rollback()
            raise

    '''
    def db_connect(self):
        engine = create_engine(self.db_engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    '''

metadata = declarative_base(cls=db_base)
metadata.query = session.query_property()



