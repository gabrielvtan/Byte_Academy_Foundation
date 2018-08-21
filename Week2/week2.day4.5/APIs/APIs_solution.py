import requests
import json
from pprint import pprint

#1) use requests to download the html document hosted at www.example.com and 
# print the html code to the screen
response = requests.get("http://www.example.com")
#print(response.text)

#2) use requests to download the json document hosted at 
# "http://dev.markitondemand.com/Api/v2/Quote/json?symbol=IBM"
response2 = requests.get("http://dev.markitondemand.com/Api/v2/Quote/json?symbol=IBM")

#THIS IS HOW YOU GO DIRECTLY FROM JSON TO DICT W/O CONVERTING A STRING
#data2 = response2.json()
#pprint(data2)

#3) use json.loads to convert that output to a dictionary and then find the 
# LastPrice value
response2 = (json.loads(response2.text))
#print(response2["LastPrice"])

#4) write a function quote(ticker_symbol) that outputs the last price of a given stock

def quote():
    ticker_symbol = input("Give me a ticker symbol: \n")
    parameters = {"symbol": ticker_symbol}
    response3 = requests.get("http://dev.markitondemand.com/Api/v2/Quote/json?", params = parameters)
    data3 = response3.json()
    print(data3["LastPrice"])

quote()

