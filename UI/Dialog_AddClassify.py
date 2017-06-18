# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_AddClassify.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from QtCreator import Ui_Dialog_AddClassify

class Dialog_AddClassify(Ui_Dialog_AddClassify.Ui_Dialog_AddClassify):
    def __init__(self):
        super(Dialog_AddClassify, self).__init__()
        self.setupUi(self)
        self.addUi()

    def test(self):
        print("Hello World")

    def addUi(self):
        self.buttonBox.accepted.connect(self.test)  # 链接"添加分类"中Ok信号和槽
        self.buttonBox.rejected.connect(self.close)  # 链接"添加分类"中Cancel信号和槽