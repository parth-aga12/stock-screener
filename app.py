from flask import Flask, render_template
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import chartlib

app = Flask(__name__)

@app.route('/moving_average_consolidation')
def moving_average_consolidation():
    tickers = [ticker.replace('.csv', '') for ticker in chartlib.get_moving_average_consolidation()]
    return render_template('tickers.html', tickers=tickers, type='moving_average_consolidation')

@app.route('/consolidation')
def general_consolidation():
    tickers = [ticker.replace('.csv', '') for ticker in chartlib.get_consolidation()]
    return render_template('tickers.html', tickers=tickers, type='consolidation')

@app.route('/breakout')
def breakout():
    tickers = [ticker.replace('.csv', '') for ticker in chartlib.get_breakout()]
    return render_template('tickers.html', tickers=tickers, type='breakout')


@app.route('/snapshot')
def snapshot():
    with open('datasets/companies.csv') as f:
        companies = f.read().splitlines()
        for company in companies:
            symbol = (company.split(',')[0])
            # print(symbol)
            df = yf.download(symbol, start=one_year_ago_date())
            df.to_csv(f'datasets/daily/{symbol}.csv')
    return {
        'code': 'success'
    }

def todays_date():
    return (datetime.today()).strftime('%Y-%m-%d')

def one_year_ago_date():
    offset = pd.tseries.offsets.BusinessDay(n=1)
    return (datetime.today() - timedelta(days=365) - offset).strftime('%Y-%m-%d')

if __name__ == '__main__':
    app.run(debug=True)
