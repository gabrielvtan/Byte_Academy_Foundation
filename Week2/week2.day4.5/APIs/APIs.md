if you're caught up and want to work on APIs, here's what I'd like you to do
1) use requests to download the html document hosted at www.example.com and print the html code to the screen
2) use requests to download the json document hosted at "http://dev.markitondemand.com/Api/v2/Quote/json?symbol=IBM"
3) use json.loads to convert that output to a dictionary and then find the LastPrice value
4) write a function quote(ticker_symbol) that outputs the last price of a given stock
bonus
create an account at quandl and figure out how to get multiple days of financial data from a stock symbol with their api
https://www.quandl.com/tools/api
this will require multiple parameters in the url. when you are sending multiple parameters in a GET requests, they are often encoded like this: url.com/api?parameterOne=value&parameterTwo=value&parameterThree=value&parameterFour=value. with quandl, you're going to need to send your api key (you get it when you create an account) as one of the parameters

also you'll want to restrict the dates or number of rows on your requests. they have years of data for some of the stocks and it can be a whole lot to download & print
write a function that takes a ticker symbol and prints out the prices for that symbol for the last 28 days. calculate the average price over that time. calculate the moving averages.
super bonus:
lookup github's api & get an github api token. (settings -> developer settings) and write a function that takes a github username and returns the names of all of their public repositories
super extra ultra bonus:
create a github repo without using the website
(you're going to need more features of requests to do this)
a whole whole lot of being a developer is reading api documentation and working out how to do useful things. no two apis are exactly alike so the real skill here is learning to learn.