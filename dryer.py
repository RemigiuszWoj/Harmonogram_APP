
# class Dryer_Specyfication:
#     """Dryer Specyfication Class"""

#     def __init__(self) -> None:
#         pass


class Dryer:
    """
    Dryer Class
    
    d1 = Dryer("A1Za",{"r" : 4, 55 : "tt"},100)

    print(d1.get_model())
    print(d1.get_dryer_specification())
    print(d1.get_price())
    print(d1.get_complet_information())
    
    """

    def __init__(self, model:str, dryer_specyfication:dict, price:int) -> None:
        self._model = model
        self._dryer_specification = dryer_specyfication
        self._price = price
    
    def get_model(self) -> str:
        return self._model

    def get_dryer_specification(self) -> dict:
        return self._dryer_specification

    def get_price(self) -> int:
        return self._price

    def get_complet_information(self):
        return {
            "model" : self.get_model(),
            "dryer specification" : self.get_dryer_specification(),
            "price" : self.get_price()
        }




