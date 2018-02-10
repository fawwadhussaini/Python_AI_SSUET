
class Battery():
    def __init__(self,battery_size=60):
        self.battery_size = battery_size
        self.battery_capacity = 60


    def upgrade_battery(self,b_size):
        self.battery_size = b_size
        if self.battery_size > 60:
            self.battery_capacity = 85

    def display_battery_capacity(self):
        print ( self.battery_capacity)

    def return_battery_capacity(self):
        return self.battery_capacity

class Car():
    def __init__(self,make,model,name):
        self.make = make
        self.model = model
        self.name = name


suzuki = Car('suzuki','2010','Wagon R')
toyota = Car('toyota','2002','corolla')
kia = Car('kia','2015','Forte')

class Electric_Car(Car):

    def __init__(self,make,model,name):
        super().__init__(make,model,name)
        self.battery = Battery()
        #self.t1 = 0
tesla = Electric_Car('tesla','2018','CV50')
#t1 = str(tesla.battery.battery_capacity())
#print ('Vehicle has ', t1)
tesla.battery.display_battery_capacity()
tesla.battery.upgrade_battery(90)
tesla.battery.display_battery_capacity()

vx = Electric_Car('Honda','2017','VX')
result = vx.battery.return_battery_capacity()
print ('Result is ', result)





