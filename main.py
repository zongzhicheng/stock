# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe:
"""
from qt.window import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
