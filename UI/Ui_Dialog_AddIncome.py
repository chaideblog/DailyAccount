# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_AddIncome.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Tools import TimeTools


class Ui_Dialog_AddIncome(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Dialog_AddIncome, self).__init__()
        self.setupUi(self)

    def test(self):
        print("Hello World")

    def setupUi(self, Dialog_AddIncome):
        Dialog_AddIncome.setObjectName("Dialog_AddIncome")
        Dialog_AddIncome.resize(411, 441)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog_AddIncome)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(100, 160, 231, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_10.addWidget(self.lineEdit_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog_AddIncome)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 20, 221, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(TimeTools.getCurrentYear(), TimeTools.getCurrentMonth(), TimeTools.getCurrentDay()), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.verticalLayout_11.addWidget(self.dateEdit_2)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(Dialog_AddIncome)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(100, 350, 291, 31))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_9)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_12.addWidget(self.checkBox_2)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Dialog_AddIncome)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 20, 62, 51))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_13.addWidget(self.label_5)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(Dialog_AddIncome)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(20, 230, 62, 51))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_14.addWidget(self.label_6)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog_AddIncome)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(100, 230, 291, 101))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_4)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_15.addWidget(self.plainTextEdit_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog_AddIncome)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(100, 90, 231, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.verticalLayout_16.addWidget(self.comboBox_2)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(Dialog_AddIncome)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 90, 62, 51))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_17.addWidget(self.label_7)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(Dialog_AddIncome)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 160, 62, 51))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_18.addWidget(self.label_8)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_AddIncome)
        self.buttonBox.setGeometry(QtCore.QRect(230, 400, 164, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.buttonBox.accepted.connect(self.test)  # 链接"添加收入"中Ok信号和槽
        self.buttonBox.rejected.connect(self.close)  # 链接"添加收入"中Cancel信号和槽

        self.retranslateUi(Dialog_AddIncome)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AddIncome)

    def retranslateUi(self, Dialog_AddIncome):
        _translate = QtCore.QCoreApplication.translate
        Dialog_AddIncome.setWindowTitle(_translate("Dialog_AddIncome", "Dialog"))
        self.checkBox_2.setText(_translate("Dialog_AddIncome", "不关闭对话框，继续添加"))
        self.label_5.setText(_translate("Dialog_AddIncome", "日期："))
        self.label_6.setText(_translate("Dialog_AddIncome", "说明："))
        self.comboBox_2.setItemText(0, _translate("Dialog_AddIncome", "工资"))
        self.label_7.setText(_translate("Dialog_AddIncome", "分类："))
        self.label_8.setText(_translate("Dialog_AddIncome", "金额："))

