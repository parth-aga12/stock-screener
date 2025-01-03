import os
import pandas as pd
import talib as ta

def is_consolidating(df, percentage):
    recent_candlesticks = df[-7:]

    max_close =recent_candlesticks['Close'].max()
    min_close =recent_candlesticks['Close'].min()

    threshold = 1 - (percentage / 100)

    if min_close > (max_close*threshold):
        # print(f'max close: {max_close}')
        # print(f'min close: {min_close}')
        return True

    return False

def is_breaking_out(df, percentage):
    last_close = df[-1:]['Close'].values[0]

    if is_consolidating(df[:-1], percentage=percentage):
        recent_closes = df[-8:-1]

        if last_close > recent_closes['Close'].max():
            return True
        
    return False

def moving_average_consolidation(df):
    days_of_consolidation = 2
    df_15 = df[(-15-days_of_consolidation):]
    df_45 = df[(-45-days_of_consolidation):]
    moving_av_15 = ta.EMA(df_15['Close'], timeperiod=5).dropna()
    # moving_av_30 = ta.EMA(recent_df['Close'], timeperiod=30).dropna()
    moving_av_45 = ta.EMA(df_45['Close'], timeperiod=13).dropna()
    percentage_diff = abs((moving_av_15 - moving_av_45) / moving_av_45) * 100
    # Check if all points are within threshold
    if all(diff <= 2.5 for diff in percentage_diff):
        return True
    
    return False


datafiles = os.listdir('datasets/daily')
for filename in datafiles:
    df = pd.read_csv(f'datasets/daily/{filename}', skiprows=[1])

    # if is_consolidating(df, percentage=1):
    #     print(f'{filename} is consolidating')

    # if is_breaking_out(df, percentage=2):
    #     print(f'{filename} is breaking out')

    if moving_average_consolidation(df):
        print(f'{filename} moving averages are consolidating')

def get_consolidation():
    consolidation = {}
    for filename in datafiles:
        df = pd.read_csv(f'datasets/daily/{filename}', skiprows=[1])
        if is_consolidating(df, percentage=1):
            consolidation[filename] = 'consolidating'
    return consolidation

def get_breakout():
    breakout = {}
    for filename in datafiles:
        df = pd.read_csv(f'datasets/daily/{filename}', skiprows=[1])
        if is_breaking_out(df, percentage=2):
            breakout[filename] = 'breaking out'
    return breakout

def get_moving_average_consolidation():
    consolidation = {}
    for filename in datafiles:
        df = pd.read_csv(f'datasets/daily/{filename}', skiprows=[1])
        if moving_average_consolidation(df):
            consolidation[filename] = 'moving averages consolidating'
    return consolidation