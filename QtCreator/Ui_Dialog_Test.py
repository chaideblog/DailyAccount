# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_test.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Test(QtWidgets.QDialog):
    def setupUi(self, Dialog_Test):
        Dialog_Test.setObjectName("Dialog_Test")
        Dialog_Test.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog_Test)
        self.label.setGeometry(QtCore.QRect(160, 115, 60, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_Test)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Test)

    def retranslateUi(self, Dialog_Test):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Test.setWindowTitle(_translate("Dialog_Test", "Dialog"))
        self.label.setText(_translate("Dialog_Test", "测试"))

