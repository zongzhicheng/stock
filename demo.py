import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import tushare as ts
import easyquotation
from script.real_time import *
import sys


# ts.set_token('4f4378e8ca037cb5142927f8e43dfdf1437fbd8be7a3bdda3cfd7a69')
# pro = ts.pro_api()
# data = pro.stock_basic(exchange='', ts_code='000001',
#                        fields='ts_code,symbol,name,area,industry,fullname,enname,cnspell,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
# print(data)

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        # 设置标题
        self.setWindowTitle('QThread多线程例子')

        # 实例化多线程对象
        self.thread = Worker()

        # 实例化列表控件与按钮控件
        self.listFile = QListWidget()
        self.btnStart = QPushButton('开始')

        # 把控件放置在栅格布局中
        layout = QGridLayout(self)
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 1)

        # 信号与槽函数的连接
        self.btnStart.clicked.connect(self.slotStart)
        self.thread.sinOut.connect(self.slotAdd)

    def slotAdd(self, file_inf):
        # 向列表控件中添加条目
        self.listFile.addItem(file_inf)

    def slotStart(self):
        # 开始按钮不可点击，线程开始
        self.btnStart.setEnabled(False)
        self.thread.start()


class Worker(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        # 设置工作状态与初始num数值
        self.working = True
        self.num = 0

    def __del__(self):
        # 线程状态改变与线程终止
        self.working = False
        self.wait()

    def run(self):
        while self.working == True:
            # 获取文本
            file_str = 'File index{0}'.format(self.num)
            self.num += 1
            # 发射信号
            self.sinOut.emit(file_str)
            # 线程休眠2秒
            self.sleep(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWidget()
    demo.show()
    sys.exit(app.exec_())
