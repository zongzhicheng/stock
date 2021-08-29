import baostock as bs


def _query_history_k_data_plus(code, fields, start_date, end_date, frequency, adjustflag):
    """
    获取历史A股K线数据
    :param code:
    :param fields:
    :param start_date:
    :param end_date:
    :param frequency:
    :param adjustflag:
    :return:
    """
    bs.query_history_k_data_plus(code, fields, start_date, end_date, frequency, adjustflag)
