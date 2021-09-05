TS_TOKEN = '4f4378e8ca037cb5142927f8e43dfdf1437fbd8be7a3bdda3cfd7a69'
DAY_PRICE_URL = 'http://api.finance.ifeng.com/%s/?code=%s&type=last'


INDEX_LABELS = ['sh', 'sz']
FIELDS = [
    # 日线指标参数
    "date, code, open, high, low, close, preclose, volume, amount, adjustflag, turn, tradestatus, pctChg, isST",
    # 周、月线指标参数
    "date, code, open, high, low, close, volume, amount, adjustflag, turn, pctChg",
    # 5、15、30、60分钟线指标参数
    "date, time, code, open, high, low, close, volume, amount, adjustflag"
]
