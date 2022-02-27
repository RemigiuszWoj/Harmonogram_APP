class Worker():
    def __init__(self, worker_id:int, first_name:str, last_name:str,
                 telephone:int, addres:str, email:str, role_1:str,role_2:str) -> None:
        self.worker_id = worker_id
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.addres = addres
        self.email = email
        self.role_1 = role_1
        self.role_2 = role_2

    def get_worker_id(self) -> int:
        return self.worker_id

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

    def get_role(self) -> tuple:
        return (self.role_1, self.role_2)

    def get_complet_information(self) -> dict:
        return {"first_name" : self.first_name,
                "last_name" : self.last_name,
                "telephone" : self.telephone,
                "addres" : self.addres,
                "email" : self.email,
                "role" : self.get_role()}