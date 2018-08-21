#bonus
import requests
import json
from pprint import pprint

# write a function that takes a ticker symbol and prints out the prices for 
# that symbol for the last 28 days. calculate the average price over that time. 
# calculate the moving averages.

def get_closing_price():
    ticker = input("Give me the ticker: \n")
    start_date = "2017-12-31"
    end_date = "2018-06-30"
    key = "VfTJzYEZLzxyaKsFmHDf"

    #Grab multiple days of financial data
    parameters = { "start_date": start_date , "end_date": end_date, "api_key": key}
    response = requests.get("https://www.quandl.com/api/v3/datasets/EOD/{}.json?".format(ticker), params = parameters)
    data = response.json()
    date_list = []
    price_list = []
    for date in range(len(data['dataset']['data'])):
        date_list.append(data['dataset']['data'][date][0])
        price_list.append(data['dataset']['data'][date][11])
        date_price_zip = dict(zip(date_list,price_list))
    return date_price_zip
 
def moving_average():
    #grab date_price_zip from get_closing_price():
    data_price_zip = get_closing_price()
    data_price_sum = sum(data_price_zip.values())
    # this returns just the average price not moving average
    return data_price_sum/len(data_price_zip)





 
#super bonus:
#lookup github's api & get an github api token. (settings -> developer settings) 
# and write a function that takes a github username and returns the names of all of 
# their public repositories

#super extra ultra bonus:
#create a github repo without using the website
#(you're going to need more features of requests to do this)
#a whole whole lot of being a developer is reading api documentation and 
# working out how to do useful things. no two apis are exactly alike so the 
# real skill here is learning to learn.