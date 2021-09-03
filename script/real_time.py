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
    for field in fields:
        if code in result:
            if isinstance(result[code][field], datetime.datetime):
                data_list.append(result[code][field].strftime('%Y-%m-%d %H:%M:%S'))
            else:
                data_list.append(result[code][field])
    return data_list


def alert_real_time_single_field(source, code, field, threshold, rule="low"):
    """
    判断实时数据filed是否大于或小于某阈值
    :param source: 
    :param code: 
    :param field: 
    :param threshold: 
    :param rule: 
    :return: 
    """""
    result = get_real_time_single_stock(source, code)
    if code not in result:
        return "codeError"
    if field not in result[code]:
        return "fieldError"
    if (rule == "low" and float(result[code][field]) < threshold) or (
            rule == "high" and float(result[code][field]) > threshold):
        flag = True
    else:
        flag = False
    return flag


if __name__ == '__main__':
    fields = ["name", "now", "close", "open", "high", "low", "datetime", "涨跌", "涨跌(%)"]
    print(show_real_time_single_stock('tencent', 'sh000001', fields))
    print(alert_real_time_single_field('tencent', 'sh000001', "涨跌(%)", 5, "low"))
