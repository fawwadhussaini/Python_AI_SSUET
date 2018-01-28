# 8.1

def display_message ():
    print ('we are learning about functions')

display_message()
print ('**********************************')
# 8.2
def favourite_book(title):
    print ('One of my favourite book is ', title)

favourite_book('Alice in wonderland')
print ('**********************************')

# 8.3

def make_shirt(size,message):
    print ('size is ' , size , 'message is: ', message)

make_shirt(16,'I am not alone')
make_shirt(message = 'Be united', size = 24)
print ('**********************************')

# 8.4

def make_shirts (message = 'i love python', size = 'large'):
    if (size == 'large' or size == 'medium'):
        message = 'I love python'

    print ('size is ' , size , 'message is: ', message)

make_shirts('Australia','medium')
make_shirts('Tom & Jerry','small')
make_shirts('This is Pakistan')
print ('**********************************')

# 8.5 Cities
def describe_city(city,country = 'Pakistan'):
    print (city + ' is situated in ' + country)

describe_city('Abuja','Nigeria')
describe_city('Karachi')
describe_city('Barcelona','Spain')

# 8.6
def city_country(city,country):
    print (city.title() + ', '+ country.title())

city_country('islamabad','pakistan')
city_country('delhi','india')
print ('**********************************')

# 8.7
def make_album(artist,title,track = ' '):
    album = {'artist_name':artist,'album_title':title,'tracks':track}
    if album['tracks'] != ' ':
        print ('Artist Name:', album['artist_name'], 'Album Title:', album['album_title'], 'Tracks:', album['tracks'])
    else:
        
        print ('Artist Name:', album['artist_name'], 'Album Title:', album['album_title'])

make_album ('Ali Zafar','Sukoon','10')
make_album ('Ali Azmat','Junoon')
make_album ('Atif Aslam','Doori','5')

# 8.8

def user_input():
    print ('**********************************')
    print ('Enter quit to exit')
    a = ' '
    t = ' '
    while a != 'quit':
        a = input ('Enter Artist Name')
        if a != 'quit':
            t = input ('Enter Album Title')
            album = {'artist_name': a, 'album_title': t}
            #return album
            print ('**********************************')
            print ('Artist Name:', album['artist_name'], 'Album Title:', album['album_title'])
            print ('**********************************')
# funcation call for exercise 8.8
user_input()

# exercise 8.9 Magicians

magicians = ['albert','russel','kenneth','peter']

def show_magician(magicians_list):
    print ('we have following magicians in our show \n', magicians_list)
print ('**********************************')
show_magician(magicians)
greetings = []
print ('**********************************')
# exercise 8.10
def make_greet():
    list_length = len(magicians)

    for m in range(list_length):
        greetings.append('Hi! Mr. ' + magicians[m].title() + ' Good Luck for your performance!')

make_greet()
show_magician(greetings)
print ('Original list of magicians intact!',magicians)

print ('**********************************')

# exercise 8.12
def sandwiches(*items):
    print ('you ordered following items:\n', items)

sandwiches('chicken','mustard souce','mayonese')
sandwiches('beef','garlic souce')
sandwiches('steam chicken','mushrooms','green beans')

# exercise 8.13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',location='princeton',domain='physics',qualification='MS')
print(user_profile)
user_profile = build_profile('fawwad','hussaini',location='Karachi',domain='Telematics',qualification='BE')
print(user_profile)

#exercise 8.14
def build_car(manufacture, model, **user_info):
    profile = {}
    profile['Car_Manufacturer'] = manufacture
    profile['Car_Model'] = model
    for key, value in user_info.items():
        profile[key] = value
    return profile

car_profile = build_car('Toyota','2007',brand = 'Vitz', color = 'Red', Transmission = 'automatic')
print (car_profile)
car_profile = build_car('Toyota','2012',brand = 'Camry', color = 'Blue')
print (car_profile)
car_profile = build_car('suzuki','2016',brand = 'Hustler', color = 'gray', Transmission = 'manual')
print (car_profile)

