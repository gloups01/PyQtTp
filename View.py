#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class View(QMainWindow) :
	
	def __init__(self):
		QMainWindow.__init__(self)
		self.createWidgets()
		self.connectWidgets()
		
		
	def createWidgets(self):
		#Création du widget conteneur de la fenetre principale et de son layout
		self.containWidget = QWidget(self)
		self.setCentralWidget(self.containWidget)
		self.layoutContain = QGridLayout()
		
		#Création du highWidget
		self.highWidget = QWidget(self.containWidget)
		self.highWidget.setStyleSheet("background-color:rgb(255,255,0)")
		self.layoutHigh = QHBoxLayout()
		self.editWho = QLineEdit("Who ?")
		self.editWho.setStyleSheet("background-color:rgb(255,255,255)")
		self.editWhere = QLineEdit("Where ?")
		self.editWhere.setStyleSheet("background-color:rgb(255,255,255)")
		self.search = QPushButton()
		
		#Création du widget de gauche
		self.leftWidget = QWidget()
		self.newContact = QPushButton("New contact")
		self.addContact = QPushButton("Add contact")
		self.layoutLeft = QVBoxLayout()
		
		#Création du widget de droite
		self.rightWidget = QScrollArea()
		
		#Création du central Widget
		self.centralWidget = QWidget(self.containWidget)
		self.layoutCentral = QGridLayout()
		
		#layout de gauche
		self.layoutLeft.addWidget(self.newContact)
		self.layoutLeft.addWidget(self.addContact)	
		self.leftWidget.setLayout(self.layoutLeft)
		
		#layout central
		self.layoutCentral.addWidget(self.leftWidget,0,0,0,1)
		self.layoutCentral.addWidget(self.rightWidget,0,1,0,7)		
		self.centralWidget.setLayout(self.layoutCentral)
		
		#layout haut
		self.layoutHigh.addWidget(self.editWho)
		self.layoutHigh.addWidget(self.editWhere)
		self.layoutHigh.addWidget(self.search)
		self.highWidget.setLayout(self.layoutHigh)
		
		#layout principal
		self.layoutContain.addWidget(self.centralWidget,1,0,6,0)
		self.layoutContain.addWidget(self.highWidget,0,0)
		self.containWidget.setLayout(self.layoutContain)
		
		#setSpacing(0)
		#setMagin(0)
		#flaticon -> créatin d'icone
		#sqllite pour base de donné
		
	def connectWidgets(self) :
		pass
		
	def slot_ajouter(self) :
		pass	
		
		
