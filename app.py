import os
import yfinance as yf
import pandas as pd
import talib
from flask import Flask,render_template, request
from patterns import pattern
app = Flask(__name__)

@app.route("/")
def hello_world():
    pattern=request.args.get('pattern')
    if pattern:
        datafiles = os.listdir('datasets/daily_data')
        for filename in datafiles:
            df = pd.read_csv('datasets/daily_data/{}'.format(filename))
            pattern_function=getattr(talib,pattern)
            result=talib.CDL3OUTSIDE(df['open'],df['High'],df['Low'],df['Close'])
    return render_template('index.html', data=pattern)

@app.route("/checkout")
def checkout():
    with open('datasets/nifty50.csv') as f:
        companies=f.read().splitlines()
        for i in companies:
            symbol=i.split(',')[0]
            df=yf.download(symbol, start="2022-01-01", end="2022-03-01")
            df.to_csv('datasets/daily_data/{}.csv'.format(symbol))


    return {
        'code ':'success'
    }

if __name__ =="__main__":
    app.run(debug=True)