import baostock as bs


def login():
    """
    登入
    :return:
    """
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond error_msg:' + lg.error_msg)


def logout():
    """
    登出
    :return:
    """
    bs.logout()
