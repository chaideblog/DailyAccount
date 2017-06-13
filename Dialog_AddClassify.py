# -*- coding: utf-8 -*-

from Ui_Dialog_AddClassify import Ui_Dialog_AddClassify
from PyQt5.QtWidgets import QDialog

class Dialog_AddClassify(QDialog, Ui_Dialog_AddClassify):
	def __init__(self):
		super(Dialog_AddClassify, self).__init__()
		self.setupUi(self)
