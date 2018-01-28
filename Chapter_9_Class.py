# Exercise 9.1 , 9.2 ,
class Restaurant():

    def __init__(self,name,cusine_type):
        self.name = name
        self.cusine_type = cusine_type
        self.customers = 0
    def describe_restaurant(self):
        print ('Restaurant Name is ', self.name)
        print ('Restaurant Cusine is ', self.cusine_type)
    def open_restaurant(self):
        print ('...Restaurant is open...')
    def set_customers_served(self,cs):
        self.customers = cs
    def increment_customers_served(self,more_customers):
        self.customers += more_customers
        print ('We have served ' + str (self.customers) + ' numbers of customers')

bella = Restaurant('BellaVita','Italian')
ginsoy = Restaurant ('Ginsoy','Chinese')

#print (bella.location)
restaurant = Restaurant('Paramount','Labenese')
print ('Restaurant is ', restaurant.name)
print ('Restaurant speciality is ', restaurant.cusine_type)
restaurant.set_customers_served(200)
restaurant.increment_customers_served(10)
print ('************************')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print ('************************')
bella.describe_restaurant()
print ('************************')
ginsoy.describe_restaurant()
ginsoy.set_customers_served(30)
ginsoy.increment_customers_served(10)

class User():
    def __init__(self,f_name,l_name):
        self.first_name = f_name
        self.last_name = l_name
        self.login_attempts = 0
#    age = ''
#    nationality = ''
#    martial_status = ''

    def describe_user(self):
        print ('User Name is ' + self.first_name.title() + ' ' + self.last_name.title())
        print (self.first_name + ' ' + self.last_name + ' is ' + self.age + ' years old')
        print (self.first_name + ' ' + self.last_name + ' is '+ self.nationality)
        print ('User is '+ self.martial_status)

    def greet_user(self):
        print ('Good Evening! Mr. '+ self.first_name + ' ' + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
        print ('This is '+ self.first_name + ' ' + self.last_name + ' ' + str(self.login_attempts) + ' login attempt')

    def reset_login_attempts(self):
        self.login_attempts = 0

student1 = User('fawwad','hussaini')
student1.age = '32'
student1.nationality = 'Pakistani'
student1.martial_status = 'Married'
student1.increment_login_attempts()
student1.increment_login_attempts()
student1.reset_login_attempts()
student1.increment_login_attempts()
student2 = User('Aamir','Iqbal')
student2.age = '28'
student2.martial_status = 'single'
student2.nationality = 'Nigerian'

student1.greet_user()
student1.describe_user()
print ('**************************')

student2.greet_user()
student2.describe_user()

# 9.5 Login Attempts



