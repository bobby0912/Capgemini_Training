transaction={}

import datetime as dt
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


class Orders:
    static_var=100
    def __init__(self,**kwargs):
        self.order_id=self.static_var
        Orders.static_var+=1
        self.orderStatus='confrimed'
        self.orderDate=dt.datetime.now()
        if 'items' in kwargs:
            self.items=kwargs['items']
    def orderDetails(self):
        print(self.order_id,self.items,self.orderStatus)

c1=Customers(name='alice')
# c1.customerDetails()

o1=Orders(items=['eggs','milk'])
# o1.orderDetails()

transaction[c1.customer_id].append(o1)

for [a,b] in transaction:
    print(a,b.orderDeatils())







    

    





# c1=Customers(name='alice')
# print(c1.customer_id)

# c2=Customers(name='bob')
# print(c2.customer_id)



    
        