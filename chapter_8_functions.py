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
