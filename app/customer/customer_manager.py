class CustomerManager:
    customers = None

    def get_customer(self, id):
        if self.customers != None:
            for item in self.customers:
                if item.id == id:
                    return item
        return None

    def get_customers(self):
        return self.customers

    def add_customer(self, newCustomer):
        if self.customers == None:
            self.customers = []
        newCustomer.id = len(self.customers)+1
        self.customers.append(newCustomer)
        return newCustomer

    def update_customer(self, customer):
        if self.customers != None and customer != None and customer.id:
            for i in range(len(self.customers)):
                if self.customers[i].id == id:
                    self.customers[i].id = customer
                    return True
        else:
            return False
