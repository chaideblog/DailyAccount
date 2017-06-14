#!/usr/bin/python3
#-*- coding:utf-8 -*-

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI import Ui_MainWindow, Ui_Dialog_AddClassify, Ui_Dialog_AddIncome, Ui_Dialog_AddSpending

def test():
    print('Hello World!')

def show_Dialog_AddClassify():
    dialog_AddClassify = Ui_Dialog_AddClassify.Ui_Dialog_AddClassify()
    if dialog_AddClassify.exec_():
        dialog_AddClassify.setupUi()
        dialog_AddClassify.show()
    dialog_AddClassify.destroy()

def show_Dialog_AddIncome():
    dialog_AddIncome = Ui_Dialog_AddIncome.Ui_Dialog_AddIncome()
    if dialog_AddIncome.exec_():
        dialog_AddIncome.setupUi()
        dialog_AddIncome.show()
    dialog_AddIncome.destroy()

def show_Dialog_AddSpending():
    dialog_AddSpending = Ui_Dialog_AddSpending.Ui_Dialog_AddSpending()
    if dialog_AddSpending.exec_():
        dialog_AddSpending.setupUi()
        dialog_AddSpending.show()
    dialog_AddSpending.destroy()

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mianWindow = Ui_MainWindow.Ui_MainWindow()
    mianWindow.Button_AddClassify.clicked.connect(show_Dialog_AddClassify)
    mianWindow.Button_AddIncome.clicked.connect(show_Dialog_AddIncome)
    mianWindow.Button_AddSpending.clicked.connect(show_Dialog_AddSpending)
    mianWindow.show()

    sys.exit(myapp.exec_())
