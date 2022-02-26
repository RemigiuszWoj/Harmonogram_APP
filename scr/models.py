from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import client
import workers

engine = create_engine("sqlite:///db.sqlite", echo=True)

Base = declarative_base()

class ClientDB(Base):
    __tablename__ = "Clients"
    client_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    telephone = Column(Integer)
    addres = Column(String)
    email = Column(String)
    nip = Column(String)

    def __init__(self,client_id:int, first_name:str, last_name:str, telephone:int, addres:str, email:str, nip:int) -> None:
        self.client_id = client_id
        self._first_name = first_name
        self._last_name = last_name
        self._telephone = telephone
        self._addres = addres
        self._email = email
        self._nip = nip

    def get_client_id(self) -> int:
        return self.client_id

    def get_first_name(self) -> str:
        return self._first_name
    
    def get_last_name(self) -> str:
        return self._last_name
    
    def get_telephone(self) -> int:
        return self._telephone

    def get_addres(self) -> str:
        return self._addres

    def get_email(self) -> str:
        return self._email

    def get_nip(self) -> str:
        return self._nip

    def get_complet_information(self) -> dict:
        return {
            "client_id" :self.client_id,
            "first_name" : self._first_name,
            "last_name" : self._last_name,
            "telephone" : self._telephone,
            "addres" : self._addres,
            "email" : self._email,
            "nip" : self._nip
        }

class Workers_DB(Base):
    __tablename__ = "Workers"
    worker_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    telephone = Column(Integer)
    addres = Column(String)
    email = Column(String)
    role_1 = Column(String)
    role_2 = Column(String)

    def __init__(self, worker_id:int, first_name:str, last_name:str, telephone:int, addres:str, email:str, role_1:str,role_2:str) -> None:
        self.worker_id = worker_id
        self._first_name = first_name
        self._last_name = last_name
        self._telephone = telephone
        self._addres = addres
        self._email = email
        self._role_1 = role_1
        self._role_2 = role_2

    def get_worker_id(self) -> int:
        return self.worker_id

    def get_first_name(self) -> str:
        return self._first_name
    
    def get_last_name(self) -> str:
        return self._last_name
    
    def get_telephone(self) -> int:
        return self._telephone

    def get_addres(self) -> str:
        return self._addres

    def get_email(self) -> str:
        return self._email

    def get_role(self) -> tuple:
        return (self._role_1, self._role_2)

    def get_complet_information(self) -> dict:
        return {
            "first_name" : self._first_name,
            "last_name" : self._last_name,
            "telephone" : self._telephone,
            "addres" : self._addres,
            "email" : self._email,
            "role" : self.get_role()
        }



Base.metadata.create_all(engine)
