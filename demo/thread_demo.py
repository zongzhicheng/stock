# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: qt线程小demo
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class Thread(QThread):
    # 线程值信号
    valueChange = pyqtSignal(int)

    # 构造函数
    def __init__(self):
        super(Thread, self).__init__()
        self.isPause = False
        self.isCancel = False
        self.cond = QWaitCondition()
        self.mutex = QMutex()
        # 暂停

    def pause(self):
        print("线程暂停")
        self.isPause = True

    # 恢复
    def resume(self):
        print("线程恢复")
        self.isPause = False
        self.cond.wakeAll()

    # 取消
    def cancel(self):
        print("线程取消")
        self.isCancel = True

    # 运行(入口)
    def run(self):
        for i in range(100):
            # 线程锁on
            self.mutex.lock()
            if self.isPause:
                self.cond.wait(self.mutex)
            if self.isCancel:
                self.valueChange.emit(0)
                break
            # 业务代码
            self.valueChange.emit(i)
            self.msleep(100)
            # 线程锁off
            self.mutex.unlock()


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        """控件的创建和布局"""
        self.layout = QVBoxLayout(self)
        self.progressBar = QProgressBar()
        self.btnBegin = QPushButton("开始")
        self.btnPause = QPushButton("暂停")
        self.btnPause.setEnabled(False)
        self.btnResume = QPushButton("恢复")
        self.btnResume.setEnabled(False)
        self.btnCancel = QPushButton("取消")
        self.btnCancel.setEnabled(False)
        self.layout.addWidget(self.progressBar)
        self.layout.addWidget(self.btnBegin)
        self.layout.addWidget(self.btnPause)
        self.layout.addWidget(self.btnResume)
        self.layout.addWidget(self.btnCancel)
        """信号绑定"""
        self.btnBegin.clicked.connect(self.__onClickedBtnbegin)
        self.btnPause.clicked.connect(self.__onClickedBtnpause)
        self.btnResume.clicked.connect(self.__onClickedBtnresume)
        self.btnCancel.clicked.connect(self.__onClickedBtncancel)

    # 开始按钮被点击的槽函数
    def __onClickedBtnbegin(self):
        self.btnBegin.setEnabled(False)
        self.btnPause.setEnabled(True)
        self.btnResume.setEnabled(False)
        self.btnCancel.setEnabled(True)
        self.thread = Thread()  # 创建线程
        self.thread.valueChange.connect(self.progressBar.setValue)  # 线程信号和槽连接
        self.thread.start()

    # 暂停按钮被点击的槽函数
    def __onClickedBtnpause(self):
        self.btnBegin.setEnabled(False)
        self.btnPause.setEnabled(False)
        self.btnResume.setEnabled(True)
        self.btnCancel.setEnabled(True)
        self.thread.pause()

    # 恢复按钮被点击的槽函数
    def __onClickedBtnresume(self):
        self.btnBegin.setEnabled(False)
        self.btnPause.setEnabled(True)
        self.btnResume.setEnabled(False)
        self.btnCancel.setEnabled(True)
        self.thread.resume()

    # 取消按钮被点击的槽函数
    def __onClickedBtncancel(self):
        self.btnBegin.setEnabled(True)
        self.btnPause.setEnabled(False)
        self.btnResume.setEnabled(False)
        self.btnCancel.setEnabled(False)
        self.thread.cancel()


if __name__ == "__main__":
    # qt程序
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
