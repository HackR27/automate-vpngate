#!/bin/python3
## fetches the config files and descriptions from the vpngate API
import requests
import pandas as pd
from io import StringIO

def getTable():
    res = requests.get('http://www.vpngate.net/api/iphone/')
    data = pd.read_csv(StringIO(res.text[15:]))
    return data