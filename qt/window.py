from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from script.real_time import *
from qt.thread import *


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.centralWidget = QWidget()
        self.initUI()

    def initUI(self):
        # 窗口初始化
        self.resize(1024, 768)
        self.setWindowTitle('量化交易平台v1.0')
        self.setCentralWidget(self.centralWidget)

        self.initLabel()
        self.initLineEdit()
        self.initPushButton()
        self.initTableWidget()

        # 控件布局
        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.addWidget(self.label1, 0, 0)
        self.gridLayout.addWidget(self.label2, 1, 1)
        self.gridLayout.addWidget(self.line_edit1, 1, 2)
        self.gridLayout.addWidget(self.push_button1, 1, 3)
        self.gridLayout.addWidget(self.push_button2, 2, 3)
        self.gridLayout.addWidget(self.table_widget1, 2, 1, 40, 2)
        self.gridLayout.addWidget(self.label3, 0, 4)
        self.gridLayout.addWidget(self.label4, 1, 4)
        self.gridLayout.addWidget(self.line_edit2, 1, 5)
        self.gridLayout.addWidget(self.label5, 2, 4)
        self.gridLayout.addWidget(self.line_edit3, 2, 5)
        self.gridLayout.addWidget(self.label6, 3, 4)
        self.gridLayout.addWidget(self.line_edit4, 3, 5)
        self.gridLayout.addWidget(self.push_button3, 1, 6)
        self.centralWidget.setLayout(self.gridLayout)

    def initLabel(self):
        # 标签初始化
        self.label1 = QLabel('实时盯盘', self)
        self.label2 = QLabel('股票代码：', self)
        self.label3 = QLabel('自动盯盘', self)
        self.label4 = QLabel('股票代码：', self)
        self.label5 = QLabel('价位：', self)
        self.label6 = QLabel('low or high', self)

    def initLineEdit(self):
        # 文本框初始化
        self.line_edit1 = QLineEdit(self)
        self.line_edit1.setText('sh000001')
        self.line_edit2 = QLineEdit(self)
        self.line_edit2.setText('sh000001')
        self.line_edit3 = QLineEdit(self)
        self.line_edit4 = QLineEdit(self)
        self.line_edit4.setText('low')

    def initPushButton(self):
        # 按钮初始化
        self.push_button1 = QPushButton('查询实时数据', self)
        self.push_button1.clicked.connect(self.__btn1Clicked)
        self.push_button2 = QPushButton('清除', self)
        self.push_button2.clicked.connect(self.__btn2Clicked)
        self.push_button3 = QPushButton('盯盘', self)

    def initTableWidget(self):
        # 表格初始化
        self.table_widget1 = QTableWidget(9, 1, self)
        self.table_widget1.setVerticalHeaderLabels(["股票名称", "现价", "昨收", "今开", "最高", "最低", "当前时间", "涨跌", "涨跌(%)"])
        self.table_widget1.setHorizontalHeaderLabels([""])
        # 将表格变为禁止编辑
        self.table_widget1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 表格头隐藏
        self.table_widget1.horizontalHeader().setVisible(False)
        # 行列自适应伸缩
        self.table_widget1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget1.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    """
    按钮点击事件
    """

    def __btn1Clicked(self):
        if self.line_edit1.text().strip() == '':
            QMessageBox.question(self, ' ', "请填写股票代码", QMessageBox.Yes, QMessageBox.Yes)
            return
        self.flag = False
        self.push_button1.setEnabled(False)
        self.thread1 = Thread1(self.line_edit1.text().strip())
        self.thread1.sinOut.connect(self.sinOutMethod)
        self.thread1.errorOut.connect(self.errorOutMethod)
        self.thread1.start()

    def __btn2Clicked(self):
        self.thread1.cancel()
        self.push_button1.setEnabled(True)
        self.line_edit1.clear()
        self.table_widget1.clearContents()

    def sinOutMethod(self, var):
        """
        sinOut触发
        :param var:
        :return:
        """
        self.table_widget1.setItem(var[0], var[1], var[2])

    def errorOutMethod(self, str):
        QMessageBox.question(self, ' ', str, QMessageBox.Yes, QMessageBox.Yes)
        self.line_edit1.clear()
        self.push_button1.setEnabled(True)

    """
    退出确认
    """

    def closeEvent(self, event):
        """
        退出确认
        :param event:
        :return:
        """
        reply = QMessageBox.question(self, ' ', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
