transaction={}

import datetime as dt
import Customers as c


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


c1=c.Customers(name='alice')
# c1.customerDetails()    

o1=Orders(items=['eggs','milk'])
# o1.orderDetails()

# print(c1.customer_id)
transaction[c1]=[]
transaction[c1].append(o1)

for [i,j] in transaction.items():   
    for order in j:
        i.customerDetails()
        order.orderDetails()







    

    





# c1=Customers(name='alice')
# print(c1.customer_id)

# c2=Customers(name='bob')
# print(c2.customer_id)



    
        