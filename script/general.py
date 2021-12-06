# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: 一些基础的公共方法
"""
import datetime
import time

E000001 = "script.real_time.alert_real_time_single_field return fieldError"


def is_number(s):
    """
    判断字符串是否为数字
    :param s:
    :return:
    """
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def compare_time(t1, t2):
    """
    判断两个时间的先后
    若 t1 >= t2，返回 True，否则返回 False
    :param t1: 格式为'%Y-%m-%d %H:%M:%S',例如：2021-12-03 13:00:00
    :param t2: 格式为'%Y-%m-%d %H:%M:%S'
    :return:
    """
    if isinstance(t1, str) and isinstance(t1, str):
        format_pattern = '%Y-%m-%d %H:%M:%S'
        dt1 = datetime.datetime.strptime(t1, format_pattern)
        dt2 = datetime.datetime.strptime(t2, format_pattern)
        if (dt1 - dt2).days > 0 and (dt1 - dt2).seconds > 0:
            return True
        else:
            return False
    else:
        return False


def judge_time_is_tradable():
    """
    判断当前时间是否在交易时间
    交易时间为 9:30-11:30、13:00-15:00
    :param t1:
    :return:
    """
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if "13:00:00" <= time_now <= "15:00:00" or "09:30:00" <= time_now <= "11:30:00":
        return True
    else:
        return False


if __name__ == '__main__':
    print(judge_time_is_tradable())
