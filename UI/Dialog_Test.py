# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Test.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from QtCreator import Ui_Dialog_Test
from Tools import TimeTools
from PyQt5 import QtCore

class Dialog_Test(Ui_Dialog_Test.Ui_Dialog_Test):
    def __init__(self):
        super(Dialog_Test, self).__init__()
        self.setupUi(self)
        self.addUi()

    def test(self):
        print("Hello World")

    def addUi(self):
        pass


