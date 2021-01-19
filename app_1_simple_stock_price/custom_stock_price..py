import yfinance as yf
import streamlit as st

st.write("""
# Stock Price App

#Shown are the stock **closing price** and ***volume*** of NATI!

""")

#define the ticker symbo

input_ticker = "NATI"
tickerSymbol = st.text_area("Input Ticker",input_ticker,height=50)
st.header('Input Ticker')
tickerSymbol

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2020-1-31', end='2020-5-31')

tickerData2 = yf.Ticker("TSLA")
tickerDf2 = tickerData2.history(period='1d', start='2020-1-31', end='2020-5-31')
st.line_chart(tickerDf2.Close)
# Open	High	Low	Close	Volume	Dividends	Stock Splits
# REMOVE COMMENT tickerData.recommendations



st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
The data above show us the fragility of the stock market and the volatility that has characterized recent times.
""")
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
