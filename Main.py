#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from View import *
from Control import *
from Model import *
import sys

def main(args) :

	app = QApplication(args)
	
	view = View()
	control = Control()
	model = Model()
	
	view.show()
	view.showMaximized()
	
	app.exec_()
	
if __name__ == "__main__" :
	main(sys.argv)
