# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_AddIncome.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from QtCreator import Ui_Dialog_AddIncome
from Tools import TimeTools
from PyQt5 import QtCore

class Dialog_AddIncome(Ui_Dialog_AddIncome.Ui_Dialog_AddIncome):
    def __init__(self):
        super(Dialog_AddIncome, self).__init__()
        self.setupUi(self)
        self.addUi()

    def test(self):
        print("Hello World")

    def addUi(self):
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(TimeTools.getCurrentYear(), TimeTools.getCurrentMonth(), TimeTools.getCurrentDay()), QtCore.QTime(0, 0, 0)))
        self.buttonBox.accepted.connect(self.test)  # 链接"添加收入"中Ok信号和槽
        self.buttonBox.rejected.connect(self.close)  # 链接"添加收入"中Cancel信号和槽

