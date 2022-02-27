class Client():
    def __init__(self, client_id:int, first_name:str, last_name:str, 
                telephone:int, addres:str, email:str, nip:int) -> None:
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.addres = addres
        self.email = email
        self.nip = nip

    def get_client_id(self) -> int:
        return self.client_id

    def get_first_name(self) -> str:
        return self.first_name
    
    def get_last_name(self) -> str:
        return self.last_name
    
    def get_telephone(self) -> int:
        return self.telephone

    def get_addres(self) -> str:
        return self.addres

    def get_email(self) -> str:
        return self.email

    def get_nip(self) -> str:
        return self.nip

    def get_complet_information(self) -> dict:
        return {"client_id" :self.client_id,
                "first_name" : self.first_name,
                "last_name" : self.last_name,
                "telephone" : self.telephone,
                "addres" : self.addres,
                "email" : self.email,
                "nip" : self.nip}