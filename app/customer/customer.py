import json
import re

class Customer:
    id = 0
    name = None
    email = None
    address = None    

    def __init__(self,name, email, address) -> None:
        self.name=name
        self.email=email
        self.address=address

    def update_name(self,name):
        if name != None and len(name)>3:
            self.name=name

    def update_email(self,email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        if email != None and re.search(regex,email):
            self.email=email

    def get_all_data_to_review(self):
        return self.__dict__

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)