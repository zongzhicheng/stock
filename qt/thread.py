# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: 线程类
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from script.real_time import *
from loguru import logger
from script.general import compare_time
import time


class Thread1(QThread):
    sinOut = pyqtSignal(tuple)
    errorOut = pyqtSignal(str)
    fields = ["name", "now", "close", "open", "high", "low", "datetime", "涨跌", "涨跌(%)"]

    # 构造函数
    def __init__(self, code):
        super(Thread1, self).__init__()
        self.code = code
        self.isCancel = False
        self.mutex = QMutex()
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def cancel(self):
        self.isCancel = True

    def run(self):
        while True:
            if self.isCancel:
                break
            # 线程锁on
            self.mutex.lock()
            result = show_real_time_single_stock('tencent', self.code, self.fields)
            if not result:
                self.errorOut.emit("股票代码格式有误（参考：sh000001）")
                break
            logger.info(result)
            time = result[6]
            if compare_time(time, self.time):
                self.time = time
                for i in range(len(result)):
                    item = QTableWidgetItem(str(result[i]))
                    var = (i - 1, 1, item)
                    # 发射信号
                    self.sinOut.emit(var)
            self.msleep(1000)
            # 线程锁off
            self.mutex.unlock()


class Thread2(QThread):
    sinOut = pyqtSignal()
    errorOut = pyqtSignal(str)
    field = "now"

    # 构造函数
    def __init__(self, code, threshold, rule):
        super(Thread2, self).__init__()
        self.code = code
        self.threshold = threshold
        self.rule = rule
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
            result = alert_real_time_single_field('tencent', self.code, self.field, self.threshold, self.rule)
            if result == "codeError":
                self.errorOut.emit("股票代码格式有误（参考：sh000001）")
                break
            if result == "filedError":
                self.errorOut.emit("请联系管理员（错误代码E000001）")
                break
            print(result)
            if result:
                self.sinOut.emit()
                self.msleep(1500)
            self.msleep(1500)
            # 线程锁off
            self.mutex.unlock()
