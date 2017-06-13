# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_addclassify.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_AddClassify(object):
    def setupUi(self, Dialog_AddClassify):
        Dialog_AddClassify.setObjectName("Dialog_AddClassify")
        Dialog_AddClassify.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog_AddClassify)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 81, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_AddClassify)
        self.buttonBox.setGeometry(QtCore.QRect(200, 240, 164, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog_AddClassify)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 20, 161, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog_AddClassify)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 160, 80, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Dialog_AddClassify)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(110, 90, 251, 51))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(Dialog_AddClassify)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(110, 160, 251, 51))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_6)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog_AddClassify)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 90, 78, 49))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)

        self.retranslateUi(Dialog_AddClassify)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AddClassify)

    def retranslateUi(self, Dialog_AddClassify):
        _translate = QtCore.QCoreApplication.translate
        Dialog_AddClassify.setWindowTitle(_translate("Dialog_AddClassify", "Dialog"))
        self.label_2.setText(_translate("Dialog_AddClassify", "类型："))
        self.comboBox_2.setItemText(0, _translate("Dialog_AddClassify", "支出"))
        self.label.setText(_translate("Dialog_AddClassify", "上级分类："))
        self.lineEdit.setText(_translate("Dialog_AddClassify", "类型："))
        self.comboBox.setItemText(0, _translate("Dialog_AddClassify", "无上级分类"))
        self.label_3.setText(_translate("Dialog_AddClassify", "分类："))

