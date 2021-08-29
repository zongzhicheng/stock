import baostock as bs


def query_k_data_history(code, fields, start_date, end_date, frequency, adjustflag):
    """
    获取历史A股K线数据
    :param code: 股票代码, sh或sz.+6位数字代码
    :param fields:
    :param start_date: 开始日期
    :param end_date: 结束日期
    :param frequency: 数据类型
            d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，不区分大小写
    :param adjustflag: 复权类型，默认不复权：3
            1：后复权；2：前复权
    :return:
    """
    return bs.query_history_k_data_plus(code, fields, start_date, end_date, frequency, adjustflag)
