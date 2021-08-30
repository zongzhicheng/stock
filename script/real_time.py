import easyquotation
import datetime


def get_real_time_single_stock(source, code):
    """
    获取单只股票实时数据
    :param source: 数据源：新浪 ['sina'] 腾讯 ['tencent', 'qq']
    :param code: 股票代码
    :return:
    """
    quotation = easyquotation.use(source)
    return quotation.real(code, prefix=True)


def get_real_time_multiple_stock(source, code_arr):
    """
    获取多个股票实时数据
    :param source: 数据源：新浪：'sina' 腾讯：'tencent', 'qq'
    :param code_arr: 多个股票代码：['000001', '162411']
    :return:
    """
    quotation = easyquotation.use(source)
    return quotation.stocks(code_arr, prefix=True)


def show_real_time_single_stock(source, code, fields):
    data_list = []
    result = get_real_time_single_stock(source, code)
    for i in fields:
        if isinstance(result[code][i], datetime.datetime):
            data_list.append(result[code][i].strftime('%Y-%m-%d %H:%M:%S'))
        else:
            data_list.append(result[code][i])
    return data_list


if __name__ == '__main__':
    fields = ["name", "now", "close", "open", "high", "low", "datetime", "涨跌", "涨跌(%)"]
    print(show_real_time_single_stock('tencent', 'sh000001', fields))
