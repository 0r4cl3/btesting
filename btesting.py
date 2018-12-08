import configparser
import oandapy as opy
import pandas as pd

config = configparser.ConfigParser()
config.read('oanda.cfg')

oanda = opy.API(environment='practice', access_token=config['oanda']['access_token'])

data = oanda.get_history(instrument='EUR_USD', start='2016-12-08', end='2016-12-10', granularity='M1')
df = pd.DataFrame(data['candles']).set_index('time')
df.index = pd.DatetimeIndex(df.index)
df.info()
