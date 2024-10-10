class Employee:
        company_name='TCS'
        company_email='tcs@gmail.com'
        def emp_details(self, name, email):
            self.name=name
            self.email=email
        def display(self):
            print( 'company name=', Employee. company_name)
            print( 'Company Email',Employee.company_email)
            print(self.name)
            print(self.email)

obj1=Employee ()
obj1.emp_details('Amal','amal@gmail.com')
obj2=Employee ()
obj2.emp_details('Arun','arun@gmail.com')
obj1.display()
obj2.display()


# Create a class ecommerce with methods
# static variable : site name
# product_create(prod_name, price, description)
# buy_product(customer_name, address, quantity default is 1 )
# date and the time should set
# if we increase quantity price should be multiplied
# order_details()
#product_name, final_price, quantity, customer_details, delivery_date

import datetime
from datetime import timedelta
class ecommerce:
        site_name='FlipKart'
        def product_create(self,prod_name, price, description):
            self.prod_name = prod_name
            self.price = price
            self.description = description
            self.site_name = ecommerce.site_name
        def buy_product(self,customer_name, address, quantity=1):
            self.customer_name = customer_name
            self.address = address
            self.quantity = quantity
            self.date = datetime.datetime.now()
            self.final_price = self.price * self.quantity
        def order_details(self):
             print( 'Site Name =', self.site_name)
             print( 'Product Name =', self.prod_name)
             print( 'Quantity =', self.quantity)
             print( 'Total Price =', self.final_price)
             print( 'Customer Name =', self.customer_name)
             print( 'Customer Address =', self.address)
             print( 'Order Date =', self.date)
             self.date += timedelta(days = 15)
             print( 'Delivery Date =', self.date)


obj1=ecommerce()
obj1.product_create(
    prod_name='iphone15 pro',
    price=100000,
    description='Latest model smartphone with 128GB storage'
)
obj1.buy_product(
    customer_name='Manu Mathew',
    address='Nampoodiathu House',
    quantity=2
)
obj1.order_details()
