"""
一些基础的公共方法
"""
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
