class Dryer_Specyfication:
    """Dryer Specyfication Class"""

    #__slots__ = ("param_1","param_2","param_3","param_4","param_5","param_6","param_7","param_8","param_9","param_10")
    def __init__(self, param_1:bool, param_2:bool, param_3:bool, param_4:bool, param_5:bool,
     param_6:bool, param_7:bool, param_8:bool, param_9:bool, param_10:bool) -> None:

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


class Dryer:
    """
    Dryer Class
    
    d1 = Dryer("A1Za",{"r" : 4, 55 : "tt"},100)

    print(d1.get_model())
    print(d1.get_dryer_specification())
    print(d1.get_price())
    print(d1.get_complet_information())
    
    """
    _models = ("model_a", "model_b", "model_c")

    def __init__(self, model:str, price:int,
     param_1:bool, param_2:bool, param_3:bool, param_4:bool, param_5:bool,
     param_6:bool, param_7:bool, param_8:bool, param_9:bool, param_10:bool
    ) -> None:
        if model not in self._models:
            raise TypeError 
        self._model = model        
        self._price = price
        self._dryer_specification = Dryer_Specyfication(param_1,param_2,param_3,param_4,param_5,
        param_6,param_7,param_8, param_9, param_10)
    
    def get_model(self) -> str:
        return self._model

    def get_dryer_specification(self) :
        return self._dryer_specification.__dict__

    def get_price(self) -> int:
        return self._price

    def get_complet_information(self):
        return {
            "model" : self.get_model(),
            "dryer specification" : self.get_dryer_specification(),
            "price" : self.get_price()
        }

d_1 = Dryer("model_a", 1000, True, False, True, True, True, True, True, True, True, False)

# print(d_1.get_model())
# print(d_1.get_price())
#print(d_1.get_dryer_specification())
print(d_1.get_complet_information())


