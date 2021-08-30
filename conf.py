class Config:
    def __init__(self):
        self.code = "sh.000001"
        self.fields = [
            # 日线指标参数
            "date, code, open, high, low, close, preclose, volume, amount, adjustflag, turn, tradestatus, pctChg, isST",
            # 周、月线指标参数
            "date, code, open, high, low, close, volume, amount, adjustflag, turn, pctChg",
            # 5、15、30、60分钟线指标参数
            "date, time, code, open, high, low, close, volume, amount, adjustflag"
        ]
        self.start_date = '2021-08-01'
        self.end_date = '2021-08-31'
