from script.histroy import *
from script.common import *
import pandas as pd
from qt.window import *
import sys


def run(config):
    # 登陆系统
    login()
    # 获取历史K线数据
    rs = query_k_data_history(config.code, config.fields[0], config.start_date, config.end_date, "d", "3")
    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    # 结果集输出到csv文件
    # result.to_csv("k_data_history.csv", encoding="gbk", index=False)
    print(result)
    # 登出系统
    logout()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ui_Form()
    sys.exit(app.exec_())
