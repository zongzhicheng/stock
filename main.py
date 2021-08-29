import baostock as bs
import pandas as pd


class Config:
    def __init__(self):
        self.code = "sh.600000"
        self.fields = [
            # 日线指标参数
            "date, code, open, high, low, close, preclose, volume, amount, adjustflag, turn, tradestatus, pctChg, isST",
            # 周、月线指标参数
            "date, code, open, high, low, close, volume, amount, adjustflag, turn, pctChg",
            # 5、15、30、60分钟线指标参数
            "date, time, code, open, high, low, close, volume, amount, adjustflag"
        ]
        self.start_date = '2020-01-01'
        self.end_date = '2020-12-31'


def run(config):
    # 登陆系统
    bs.login()
    """
    获取历史K线数据
    
    """
    # frequency="d"取日k线adjustflag="3"默认不复权
    rs = bs.query_history_k_data_plus(config.code, config.fields[0],
                                      config.start_date, config.end_date,
                                      frequency="d", adjustflag="3")
    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("history_k_data.csv", encoding="gbk", index=False)
    print(result)

    # 登出系统
    bs.logout()


if __name__ == '__main__':
    cfg = Config()
    run(cfg)
