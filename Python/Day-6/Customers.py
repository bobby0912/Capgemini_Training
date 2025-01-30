class Customers:
    static_var=1
    def __init__(self,**kwargs):
        self.customer_id=self.static_var
        Customers.static_var+=1
        if 'name' in kwargs:
            self.name=kwargs['name']
        # if 'phone' in kwargs:
        #     self.name=kwargs['phone']
        # if 'mail' in kwargs:
        #     self.name=kwargs['mail']
        # if 'address' in kwargs:
        #     self.name=kwargs['address']
    def customerDetails(self):
        print(self.customer_id,self.name)