import models
from sqlalchemy.orm import sessionmaker

HARMONOGRAM = { 
    1 :
        {"action_id" : 1,
         "destription" : "material preparation cutting drilling milling rolling circles of the dryer",
         "work_time" : 40,
         "workers" : "UUUU",
         "delay" : "0",
         "material" : " ",
        },
    2 :
        {"action_id" : 2,
         "destription" : "preparation of welded elements such as the undercarriage with adjustable supports for the Lower Basket and the inner chamber",
         "work_time" : 30,
         "workers" : "UUUU",
         "delay" : "1(0)",
         "material" : " ",
        },
    3 :
        {"action_id" : 3,
         "destription" : "put together",
         "work_time" : 40,
         "workers" : "UUU",
         "delay" : "2(0)",
         "material" : " ",
        },
    4 :
        {"action_id" : 4,
         "destription" : "assembly of elements ordered from external companies",
         "work_time" : 16,
         "workers" : "U",
         "delay" : "3(0)",
         "material" : " ",
        },
    5 :
        {"action_id" : 5,
         "destription" : "Material order",
         "work_time" : 2,
         "workers" : "U",
         "delay" : "4(0)",
         "material" : " ",
        },
    6 :
        {"action_id" : 6,
         "destription" : "Drilling",
         "work_time" : 15,
         "workers" : "UUU",
         "delay" : "5(5 * 24)",
         "material" : " ",
        },

}


def add_element_of_harmonogram(id:int):  
    Session = sessionmaker(bind=models.engine)
    session = Session()
    harmonogram = models.Harmonogram(action_id=HARMONOGRAM[id]["action_id"],
                                     destription=HARMONOGRAM[id]["destription"],
                                     work_time=HARMONOGRAM[id]["work_time"],
                                     workers=HARMONOGRAM[id]["workers"],
                                     delay=HARMONOGRAM[id]["delay"],
                                     material=HARMONOGRAM[id]["material"],
                                    )

    session.add(harmonogram)
    session.commit()

def add_harmonogram():
    for i in HARMONOGRAM.keys():
        add_element_of_harmonogram(id=i)



