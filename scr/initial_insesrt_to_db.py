import models
import harmonogram
import create_content_to_db
from sqlalchemy.orm import sessionmaker

def initial_db_by_value(function):
    def wraper(instance_number:int):
        for i in range(1,instance_number+1,1):
            function(i)
    return wraper

@initial_db_by_value
def add_random_user(id:int):
    Session = sessionmaker(bind=models.engine)
    session = Session()
    client = models.Client(client_id=id,
                           first_name=create_content_to_db.get_first_name(),
                           last_name=create_content_to_db.get_last_name(),
                           telephone=create_content_to_db.get_telepchone(),
                           addres=create_content_to_db.get_address(),
                           email=create_content_to_db.get_email(),
                           nip=create_content_to_db.get_nip(),)
    session.add(client)
    session.commit()

@initial_db_by_value
def add_random_worker(id:int):
    Session = sessionmaker(bind=models.engine)
    session = Session()
    worker = models.Worker(worker_id=id,
                           first_name=create_content_to_db.get_first_name(),
                           last_name=create_content_to_db.get_last_name(),
                           telephone=create_content_to_db.get_telepchone(),
                           addres=create_content_to_db.get_address(),
                           email=create_content_to_db.get_email(),
                           function_1=create_content_to_db.get_function(),
                           function_2=create_content_to_db.get_function(),)
    session.add(worker)
    session.commit()

@initial_db_by_value
def add_random_dryer(id:int):
    Session = sessionmaker(bind=models.engine)
    session = Session()  
    dryer = models.Dryer(dryer_id=id,
                         model=create_content_to_db.get_dryer_model(),
                         price=create_content_to_db.get_price(),
                         elevated_mesh=create_content_to_db.get_param_bool_status(),
                         central_lubrication=create_content_to_db.get_param_bool_status(),
                         plc_control=create_content_to_db.get_param_bool_status(),
                         scada_control=create_content_to_db.get_param_bool_status(),
                         contactor_control=create_content_to_db.get_param_bool_status(),
                         gas_burner=create_content_to_db.get_param_bool_status(),
                         oil_burner=create_content_to_db.get_param_bool_status(),
                         electric_powered=create_content_to_db.get_param_bool_status(),
                         tractor_powered=create_content_to_db.get_param_bool_status(),
                         double_discharge=create_content_to_db.get_param_bool_status(),)           
    session.add(dryer)
    session.commit()

@initial_db_by_value
def add_random_item(id:int):  
    Session = sessionmaker(bind=models.engine)
    session = Session()
    if id <= len(create_content_to_db.MATERIALS):
        item = models.Item(item_id=id,
                           item_name=create_content_to_db.get_item_name(id=id),
                           item_quantity=create_content_to_db.get_item_quantity(),
                           item_price=create_content_to_db.get_item_price(),
                           deliwery_time=create_content_to_db.get_deliwery_time(),) 
                                
        session.add(item)
        session.commit()



# Session = sessionmaker(bind=models.engine)
# session = Session()

add_random_user(20)
add_random_worker(8)
add_random_dryer(5)
add_random_item(11)
harmonogram.add_harmonogram()