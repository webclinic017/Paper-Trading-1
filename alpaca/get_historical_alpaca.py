from config import API_KEY, SECRET_KEY, APCA_API_BASE_URL
from abc import ABC, abstractmethod
from __init__ import Trade
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
from datetime import datetime
from datetime import timedelta
import pandas as pd


api = tradeapi.REST(API_KEY, SECRET_KEY, APCA_API_BASE_URL, 'v2')

barset = api.get_barset("APPL", "day")

print(barset)