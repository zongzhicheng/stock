import tushare as ts
import easyquotation
from script.real_time import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget

ts.set_token('4f4378e8ca037cb5142927f8e43dfdf1437fbd8be7a3bdda3cfd7a69')
pro = ts.pro_api()
data = pro.stock_basic(exchange='', ts_code='000001',
                       fields='ts_code,symbol,name,area,industry,fullname,enname,cnspell,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
print(data)
