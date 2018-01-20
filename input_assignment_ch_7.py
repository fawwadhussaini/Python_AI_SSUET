# 7.1 Rental Car

Rental_Car = input ('Which car do you want...')
print ('Let me see, if i have '+ Rental_Car)

# 7.2 Table Request

group_of_guests = int(input ('How many people are there in your dinner invitation...'))
if group_of_guests > 8:
    print ('You will have to wait for a table!')
else:
    print ('Your table is ready!')

# 7.3 Multiple of 10

user_number = int(input('Enter your number please...'))
if user_number % 10 == 0:
    print ('You Entered ' + str(user_number) + ' it is a multiple of 10')
else:
    print ('You Entered ' + str(user_number) + ' it is not a multiple of 10')

#7.4 Pizza Toppings

flag = True
toppings = []
topping = ''
print ('Let me have you Pizza order please...\n')
while flag:
    if topping == '':
        topping = input('What would you like as Pizza topping please...')
    else:
        topping = input ('Anything else sir! ')
    if topping == 'no thanks':
        flag = False
    else:
        toppings.append(topping)

print ('As requested, following toppings has been added to your pizza', toppings[:])

# 7.5 Movie Tickets and 7.6
print ('To get the ticket, please enter your age...\n To exit, enter quit')
flag = True
count = 0
while flag:
    user_age = input('Your age please...')
    count += 1
    if user_age == 'quit':
        flag = False
        break
    if int(user_age) < 3 :
        print ('Ticket is free for you')
    elif int(user_age) > 3 and  int(user_age) < 12:
        print ('you have to pay $10')
    elif int(user_age) > 12:
        print ('you have to pay $15')
count -= 1
print ('you have '+ str(count) + ' people in the cinema')
# 7.7 loop that runs infinite times
'''
print ('To get the ticket, please enter your age...\n')
flag = True
count = 0
while flag:
    user_age = input('Your age please...')
    count += 1
    if int(user_age) < 3 :
        print ('Ticket is free for you')
    elif int(user_age) > 3 and  int(user_age) < 12:
        print ('you have to pay $10')
    elif int(user_age) > 12:
        print ('you have to pay $15')
count -= 1
print ('you have '+ str(count) + ' people in the cinema')

'''
#  7.8

sandwich_order = ['Pastrami','Cheese','Caprese','Club','Multi Deker']

finished_sandwiches = []
no_of_sandwiches = len(sandwich_order)

while no_of_sandwiches > 0:
    no_of_sandwiches -= 1
    sandwich = sandwich_order.pop()
    print ('I made your '+ sandwich +' sandwich \n')
    finished_sandwiches.append(sandwich)

print ('Finished orders are as follows\n ', finished_sandwiches[:])
print('********************************************************\n')

#7.9
sandwich_orders = ['Pastrami','Cheese','Pastrami','Caprese','Club','Pastrami','Multi Deker']
print ('The deli has run out of pastrami')
finished_sandwiches2 = []
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

finished_sandwiches2.append(sandwich_orders)

print ('Finished orders are as follows\n ', finished_sandwiches2[:])
print('********************************************************\n')

#7.10
flag = True
database ={}
print ('Enter exit, one you are done...')
while flag :
    name = input ('What is your name please!\n')
    if name == 'exit':
        break
    location = input('If you could visit one place in the world, where would you go?\n')
    database [name] = location

for k,v in database.items():
    print (k + ' would like to visit ' + v)

