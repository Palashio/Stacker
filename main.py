import yfinance as yf

msft = yf.Ticker("MSFT")

hist = msft.history()

print(hist.columns)