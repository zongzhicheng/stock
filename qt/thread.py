from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from script.real_time import *


class Thread1(QThread):
    sinOut = pyqtSignal(tuple)
    errorOut = pyqtSignal(str)
    fields = ["name", "now", "close", "open", "high", "low", "datetime", "涨跌", "涨跌(%)"]

    # 构造函数
    def __init__(self, text):
        super(Thread1, self).__init__()
        self.text = text
        self.isCancel = False
        self.mutex = QMutex()

    def cancel(self):
        self.isCancel = True

    def run(self):
        while True:
            if self.isCancel:
                break
            # 线程锁on
            self.mutex.lock()
            result = show_real_time_single_stock('tencent', self.text, self.fields)
            if not result:
                self.errorOut.emit("股票代码格式有误（参考：sh000001）")
                break
            print(result)
            for i in range(len(result)):
                item = QTableWidgetItem(str(result[i]))
                var = (i - 1, 1, item)
                # 发射信号
                self.sinOut.emit(var)
            self.msleep(1500)
            # 线程锁off
            self.mutex.unlock()
