# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)