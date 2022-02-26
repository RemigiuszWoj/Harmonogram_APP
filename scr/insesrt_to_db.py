
import models
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=models.engine)
session = Session()

client = models.ClientDB(1,"Janusz","Tracz",666555444,"Kew 12 Wrocław","ew@we.pl",3339983419)
session.add(client)

worker = models.Workers_DB(1, "Janusz","Tracz",666555444,"Kew 12 Wrocław","ew@we.pl","sp","re")
session.add(worker)

session.commit()