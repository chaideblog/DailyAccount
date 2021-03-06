#!/usr/bin/python3
#-*- coding:utf-8 -*-

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI import MainWindow, Dialog_AddClassify, Dialog_AddSpending, Dialog_AddIncome, Dialog_Test

def test():
    print('Hello World!')

def show_Dialog_AddClassify():
    dialog_AddClassify = Dialog_AddClassify.Dialog_AddClassify()
    if dialog_AddClassify.exec_():
        dialog_AddClassify.setupUi()
        dialog_AddClassify.show()
    dialog_AddClassify.destroy()

def show_Dialog_AddIncome():
    dialog_AddIncome = Dialog_AddIncome.Dialog_AddIncome()
    if dialog_AddIncome.exec_():
        dialog_AddIncome.setupUi()
        dialog_AddIncome.show()
    dialog_AddIncome.destroy()

def show_Dialog_AddSpending():
    dialog_AddSpending = Dialog_AddSpending.Dialog_AddSpending()
    if dialog_AddSpending.exec_():
        dialog_AddSpending.setupUi()
        dialog_AddSpending.show()
    dialog_AddSpending.destroy()

def show_Test(mainWindow):
    mainWindow.widget.close()

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mainWindow = MainWindow.MainWindow()
    mainWindow.Button_AddClassify.clicked.connect(show_Dialog_AddClassify)
    mainWindow.Button_AddIncome.clicked.connect(show_Dialog_AddIncome)
    mainWindow.Button_AddSpending.clicked.connect(show_Dialog_AddSpending)
    mainWindow.Button_Classify.clicked.connect(show_Test)
    mainWindow.show()

    sys.exit(myapp.exec_())