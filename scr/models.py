from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///data_base.sqlite", echo=True)

Base = declarative_base()

class Client(Base):        
    """Base CLient Class"""
    __tablename__ = "Clients"
    client_id = Column(Integer(), primary_key=True)
    first_name = Column(String(), primary_key=False)
    last_name = Column(String())
    telephone = Column(Integer())
    addres = Column(String())
    email = Column(String())
    nip = Column(String())

    def __init__(self, client_id:int, first_name:str, last_name:str, 
                telephone:int, addres:str, email:str, nip:int) -> None:
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.addres = addres
        self.email = email
        self.nip = nip

class Worker(Base):
    """Base Worker Class"""
    __tablename__ = "Workers"
    worker_id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    telephone = Column(Integer())
    addres = Column(String())
    email = Column(String())
    role_1 = Column(String())
    role_2 = Column(String())

    def __init__(self, worker_id:int, first_name:str, last_name:str,
                 telephone:int, addres:str, email:str, role_1:str,role_2:str) -> None:
        self.worker_id = worker_id
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.addres = addres
        self.email = email
        self.role_1 = role_1
        self.role_2 = role_2

class Dryer(Base):
    """Base Dryer Class"""
    __tablename__ = "Dryers"
    dryer_id = Column(Integer(), primary_key=True)
    model = Column(String())
    price = Column(Integer())
    param_1 = Column(Integer(), nullable=True)
    param_2 = Column(Integer(), nullable=True)
    param_3 = Column(Boolean(), nullable=True)
    param_4 = Column(Boolean(), nullable=True)
    param_5 = Column(Boolean(), nullable=True)
    param_6 = Column(Boolean())
    param_7 = Column(Boolean())
    param_8 = Column(Boolean())
    param_9 = Column(Boolean())
    param_10 = Column(Boolean())

    _models = ("model_a", "model_b", "model_c")

    def __init__(self, dryer_id:int, model:str, price:int,
                 param_1:bool, param_2:bool, param_3:bool, param_4:bool, param_5:bool,
                 param_6:bool, param_7:bool, param_8:bool, param_9:bool, param_10:bool) -> None:
    
        if model not in self._models:
            raise TypeError 
        self.dryer_id = dryer_id
        self.model = model        
        self.price = price
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3
        self.param_4 = param_4
        self.param_5 = param_5
        self.param_6 = param_6
        self.param_7 = param_7
        self.param_8 = param_8
        self.param_9 = param_9
        self.param_10 = param_10
    
Base.metadata.create_all(engine)
