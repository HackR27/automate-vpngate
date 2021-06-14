#!/bin/python3
## fetches the config files and descriptions from the vpngate API
import requests
import pandas as pd
import numpy as np
from io import StringIO

def getTable():
    res = requests.get('http://www.vpngate.net/api/iphone/')
    df = pd.read_csv(StringIO(res.text[15:])).fillna('9999')
    df = df[df.Ping != '-']
    df['Ping'] = df['Ping'].apply(pd.to_numeric)
    return df.sort_values(by=['Ping','Speed','TotalUsers'],ascending=[1,0,1])
    

# df = getTable()
# print(df[['IP','Speed','Ping','TotalUsers']].head())