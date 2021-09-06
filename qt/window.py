from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from qt.thread import *
from script.general import *
from PyQt5.QtCore import *
import time
import os


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.centralWidget = QWidget()
        self.initUI()
        self.player = QMediaPlayer()
        self.player.setVolume(100.0)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(os.getcwd() + "\qt\mp3\welcome.mp3")))
        self.player.play()

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
        self.gridLayout.addWidget(self.push_button4, 2, 6)
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
        self.push_button2.setEnabled(False)
        self.push_button2.clicked.connect(self.__btn2Clicked)
        self.push_button3 = QPushButton('盯盘', self)
        self.push_button3.clicked.connect(self.__btn3Clicked)
        self.push_button4 = QPushButton('清除', self)
        self.push_button4.setEnabled(False)
        self.push_button4.clicked.connect(self.__btn4Clicked)

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
        """
        查询实时数据
        :return:
        """
        if self.line_edit1.text().strip() == '':
            QMessageBox.question(self, ' ', "请填写股票代码", QMessageBox.Yes, QMessageBox.Yes)
            return
        self.push_button1.setEnabled(False)
        self.push_button2.setEnabled(True)
        self.line_edit1.setReadOnly(True)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(os.getcwd() + "\qt\mp3\stock_real_time_start.mp3")))
        self.player.play()
        self.thread1 = Thread1(self.line_edit1.text().strip())
        self.thread1.sinOut.connect(self.thread1SinOutMethod)
        self.thread1.errorOut.connect(self.thread1ErrorOutMethod)
        self.thread1.start()

    def __btn2Clicked(self):
        """
        清除
        :return:
        """
        self.thread1.cancel()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(os.getcwd() + "\qt\mp3\stock_real_time_stop.mp3")))
        self.player.play()
        self.push_button1.setEnabled(True)
        self.line_edit1.setReadOnly(False)
        self.line_edit1.clear()
        self.table_widget1.clearContents()

    def __btn3Clicked(self):
        """
        盯盘
        :return:
        """
        if self.line_edit2.text().strip() == '':
            QMessageBox.question(self, ' ', "请填写股票代码", QMessageBox.Yes, QMessageBox.Yes)
            return
        if self.line_edit3.text().strip() == '':
            QMessageBox.question(self, ' ', "请填写价位", QMessageBox.Yes, QMessageBox.Yes)
            return
        if not is_number(self.line_edit3.text().strip()):
            QMessageBox.question(self, ' ', "价位栏请填写数字", QMessageBox.Yes, QMessageBox.Yes)
            self.line_edit3.clear()
            return
        if self.line_edit4.text().strip() == '' or self.line_edit4.text().strip() not in ['low', 'high']:
            QMessageBox.question(self, ' ', "请填写'low'或者'high'", QMessageBox.Yes, QMessageBox.Yes)
            self.line_edit4.clear()
            return
        self.push_button3.setEnabled(False)
        self.push_button4.setEnabled(True)
        self.line_edit2.setReadOnly(True)
        self.line_edit3.setReadOnly(True)
        self.line_edit4.setReadOnly(True)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(os.getcwd() + "\qt\mp3\stock_auto_real_time_start.mp3")))
        self.player.play()
        self.thread2 = Thread2(self.line_edit2.text().strip(),
                               self.line_edit3.text().strip(),
                               self.line_edit4.text().strip())
        self.thread2.sinOut.connect(self.thread2SinOutMethod)
        self.thread2.errorOut.connect(self.thread2ErrorOutMethod)
        self.thread2.start()

    def __btn4Clicked(self):
        """
        清除
        :return:
        """
        self.thread2.cancel()
        self.push_button3.setEnabled(True)
        self.line_edit2.clear()
        self.line_edit3.clear()
        self.line_edit2.setReadOnly(False)
        self.line_edit3.setReadOnly(False)
        self.line_edit4.setReadOnly(False)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(os.getcwd() + "\qt\mp3\stock_auto_real_time_stop.mp3")))
        self.player.play()

    def thread1SinOutMethod(self, var):
        """
        sinOut触发
        :param var:
        :return:
        """
        self.table_widget1.setItem(var[0], var[1], var[2])

    def thread1ErrorOutMethod(self, str):
        QMessageBox.question(self, ' ', str, QMessageBox.Yes, QMessageBox.Yes)
        self.line_edit1.clear()
        self.push_button1.setEnabled(True)

    def thread2SinOutMethod(self):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(os.getcwd() + "\qt\mp3\stock_reach_threshold.mp3")))
        self.player.play()

    def thread2ErrorOutMethod(self, str):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(os.getcwd() + "\qt\mp3\stock_auto_real_time_fail.mp3")))
        self.player.play()
        QMessageBox.question(self, ' ', str, QMessageBox.Yes, QMessageBox.Yes)
        self.line_edit2.clear()
        self.line_edit3.clear()
        self.push_button3.setEnabled(True)

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
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(os.getcwd() + "\qt\mp3\goodbye.mp3")))
            self.player.play()
            QThread().msleep(2000)
            event.accept()
        else:
            event.ignore()
