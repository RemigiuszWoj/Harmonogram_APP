class Worker:
    """
    Worker class

    Use sample:

   
    K1 = Worker("Janusz","Tracz",666555444,"Kew 12 Wrocław","ew@we.pl","sp","re")

    print(K1.get_first_name())
    print(K1.get_last_name())
    print(K1.get_telephone())
    print(K1.get_addres())
    print(K1.get_email())
    print(K1.get_role())
    print(K1.get_complet_information())


    """

    def __init__(self, first_name:str, last_name:str, telephone:int, addres:str, email:str, role_1:str,role_2:str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._telephone = telephone
        self._addres = addres
        self._email = email
        self._role_1 = role_1
        self._role_2 = role_2

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


# class Workers:

#     """"Workers class"""

#     def __init__(self) -> None:
#         pass

#     def add_worker(self, worker:Worker):
#         name = worker._first_name()
#         self.name =  