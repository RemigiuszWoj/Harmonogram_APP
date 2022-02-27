
import models
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=models.engine)
session = Session()

client = models.Client(client_id=1, first_name="Janu2222sz", last_name="Tracz",
                        telephone=90890, addres="Krerw 12", email="re@wp.pl", nip=99887)
# session.add(client)

worker = models.Worker(worker_id=1, first_name="Janusz", last_name="Tracz", telephone=666555444,
                       addres="Kew 12 Wrocław", email="ew@we.pl", role_1="sp", role_2="re")
# session.add(worker)

dryer = models.Dryer(dryer_id=2, model="model_a", price=1000, param_1=True, param_2=False,
                     param_3=True, param_4=True, param_5=True, param_6=True, param_7=True,
                     param_8=True, param_9=True, param_10=False)
session.add(dryer)

session.commit()