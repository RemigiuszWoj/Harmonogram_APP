

class Client:
    """
    Client class

    Use sample:

    K1 = Client("Janusz","Tracz",666555444,"Kew 12 Wrocław","ew@we.pl",3339983419)

    print(K1.get_first_name())
    print(K1.get_last_name())
    print(K1.get_telephone())
    print(K1.get_addres())
    print(K1.get_email())
    print(K1.get_nip())
    print(K1.get_complet_information())

    """

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


