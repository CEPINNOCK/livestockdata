import yfinance as yf 


#The data requirements can match different intervals, date and time 



df = yf.Ticker('MSFT').history(period='1y')[['Close', 'Open', 'High']]


print(df)
