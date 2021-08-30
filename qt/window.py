from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from script.real_time import *
import time


class ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 窗口初始化
        self.resize(1024, 768)
        self.center()
        self.setWindowTitle('量化交易平台v1.0')

        self.initLabel()
        self.initLineEdit()
        self.initPushButton()
        self.initTableWidget()
        self.show()

    def initLabel(self):
        # 标签初始化
        self.label1 = QLabel('股票代码：', self)
        self.label1.move(30, 30)

    def initLineEdit(self):
        # 文本框初始化
        self.line_edit1 = QLineEdit(self)
        self.line_edit1.move(90, 25)
        self.line_edit1.resize(60, 20)
        self.line_edit1.setText('sh000001')

    def initPushButton(self):
        # 按钮初始化
        self.push_button1 = QPushButton('查询实时数据', self)
        self.push_button1.move(160, 25)
        self.push_button1.setCheckable(False)
        self.push_button1.clicked.connect(self.btnClicked)

    def initTableWidget(self):
        # 表格初始化
        self.table_widget1 = QTableWidget(9, 1, self)
        self.table_widget1.move(30, 60)
        self.table_widget1.resize(210, 300)
        self.table_widget1.setVerticalHeaderLabels(["股票名称", "现价", "昨收", "今开", "最高", "最低", "当前时间", "涨跌", "涨跌(%)"])
        self.table_widget1.setHorizontalHeaderLabels([""])
        # 将表格变为禁止编辑
        self.table_widget1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 表格头隐藏
        self.table_widget1.horizontalHeader().setVisible(False)
        # 行列自适应伸缩
        self.table_widget1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget1.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def btnClicked(self):
        fields = ["name", "now", "close", "open", "high", "low", "datetime", "涨跌", "涨跌(%)"]
        if self.push_button1.isChecked():
            # 已被单击
            self.push_button1.setCheckable(False)
            self.push_button1.toggle()  # 切换按钮状态
        else:
            # 未被单击
            self.push_button1.setCheckable(True)
            self.push_button1.toggle()  # 切换按钮状态
            result = show_real_time_single_stock('tencent', self.line_edit1.text().strip(), fields)
            print(result)
            for i in range(len(result)):
                # print(i)
                item = QTableWidgetItem(str(result[i]))
                self.table_widget1.setItem(i - 1, 1, item)

    def center(self):
        """
        窗口显示在屏幕的中间
        :return:
        """
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        """
        退出确认
        :param event:
        :return:
        """
        reply = QMessageBox.question(self, ' ',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
