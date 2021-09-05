import tushare as ts
from conf import *



pro = ts.pro_api(TS_TOKEN)
# print(pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date'))
print(pro.new_share(start_date='20210906', end_date='20210920'))
