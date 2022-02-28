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
    function_1 = Column(String())
    function_2 = Column(String())

    def __init__(self, worker_id:int, first_name:str, last_name:str,
                 telephone:int, addres:str, email:str, function_1:str,function_2:str) -> None:
        self.worker_id = worker_id
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.addres = addres
        self.email = email
        self.function_1 = function_1
        self.function_2 = function_2
    

class Dryer(Base):
    """Base Dryer Class"""
    __tablename__ = "Dryers"
    dryer_id = Column(Integer(), primary_key=True)
    model = Column(String())
    price = Column(Integer())
    elevated_mesh = Column(Integer())  # Column(Boolean(), nullable=True)
    central_lubrication = Column(Integer())
    plc_control = Column(Integer())
    scada_control = Column(Integer())
    contactor_control = Column(Integer())
    gas_burner = Column(Integer())
    oil_burner = Column(Integer())
    electric_powered = Column(Integer())
    tractor_powered = Column(Integer())
    double_discharge = Column(Integer())

    _models = ("dryer_20_t", "dryer_35_t", "dryer_50_t")

    def __init__(self, dryer_id:int, model:str, price:int,
                 elevated_mesh:bool, central_lubrication:bool, plc_control:bool, scada_control:bool, contactor_control:bool, gas_burner:bool, oil_burner:bool, electric_powered:bool,
                 tractor_powered:bool, double_discharge:bool) -> None:
    
        if model not in self._models:
            raise TypeError 
        self.dryer_id = dryer_id
        self.model = model        
        self.price = price
        self.elevated_mesh = elevated_mesh
        self.central_lubrication = central_lubrication
        self.plc_control = plc_control
        self.scada_control = scada_control
        self.contactor_control = contactor_control
        self.gas_burner = gas_burner
        self.oil_burner = oil_burner
        self.electric_powered = electric_powered
        self.tractor_powered = tractor_powered
        self.double_discharge = double_discharge
    

class Item(Base):
    """Base item in magasin class"""
    __tablename__ = "Magasin"
    item_id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    item_quantity = Column(Integer())
    item_price = Column(Integer())
    deliwery_time = Column(Integer())

    def __init__(self, item_id:int, item_name:str, item_quantity:int,
                 item_price:int, deliwery_time:int) -> None:
        self.item_id = item_id
        self.item_name = item_name
        self.item_quantity = item_quantity
        self.item_price = item_price
        self.deliwery_time = deliwery_time

Base.metadata.create_all(engine)