#inheritance 

#creating a class car which inherits the class vehicle

class Vehicle:
    def __init__(self,brand):
        self.brand=brand

class Car(Vehicle):
    def __init__(self,brand,name):
        self.name=name
        #super used to call the parent class attribute
        super().__init__(brand)

    def printa(self):
        print(self.brand,self.name)

a = Car('BMW','X5')
a.printa()