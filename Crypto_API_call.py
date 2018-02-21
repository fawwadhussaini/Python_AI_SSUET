import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# User Input For CryptoCurrency Conversion
From_Currency = input ('Enter your prime currency, you want to convert:')
To_Currency = input ('Enter your desired currency, you want to see result:')
Limit = input ('Enter no. of records you want to be plotted on graph:')
Limit = Limit - 1



def daily_price_history(symbol, comparison_symbol,limit=10, exchange=''):
# Parameters those will be passed with url for API call
    parameters = {'fsym':symbol,'tsym':comparison_symbol,'all_data':True,'limit':limit,'aggregate':1}
# Another parameter append in url
    if exchange:
        parameters['e']= exchange

    response = requests.get('https://min-api.cryptocompare.com/data/histominute', params=parameters)
    result = response.json()['Data']

    print (result)
    grid = pd.DataFrame(result)
# Drop irrelevent column from dataframe
    grid.drop('volumefrom',axis=1,inplace=True)
    grid.drop('volumeto', axis=1, inplace=True)
    counter = 0 # To get index of dataframe (grid)

    print ('Length is {}'.format(len(grid)))
    #print (grid.loc[3]['high'])
    for i in grid.time:

        grid.at[counter,'DateTime'] = datetime.datetime.fromtimestamp(i)
        counter += 1

    #grid['new_column'] = datetime.datetime.fromtimestamp('time')
    #print (grid)

    return grid

#print (daily_price_history('BTC',['USD']))

data_set =  daily_price_history(From_Currency,To_Currency, Limit)
plt.plot(data_set.DateTime, data_set.close)

plt.title(From_Currency + ' To ' + To_Currency)

plt.ylabel('Price In ' + To_Currency)

plt.xlabel('Duration')

plt.show()
