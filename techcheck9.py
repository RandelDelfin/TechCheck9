# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'techcheck9.ui'
#
# Created: Tue Nov 29 14:54:33 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(426, 405)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButtonCalculate = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(130, 130, 106, 33))
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.lineeditSalary = QtWidgets.QLineEdit(self.centralWidget)
        self.lineeditSalary.setGeometry(QtCore.QRect(300, 10, 113, 35))
        self.lineeditSalary.setObjectName("lineeditSalary")
        self.lineEditDependents = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEditDependents.setGeometry(QtCore.QRect(300, 60, 61, 35))
        self.lineEditDependents.setObjectName("lineEditDependents")
        self.labelSalary = QtWidgets.QLabel(self.centralWidget)
        self.labelSalary.setGeometry(QtCore.QRect(20, 10, 211, 23))
        self.labelSalary.setObjectName("labelSalary")
        self.labelDependants = QtWidgets.QLabel(self.centralWidget)
        self.labelDependants.setGeometry(QtCore.QRect(20, 70, 271, 23))
        self.labelDependants.setObjectName("labelDependants")
        self.labelOutput = QtWidgets.QLabel(self.centralWidget)
        self.labelOutput.setGeometry(QtCore.QRect(10, 170, 401, 181))
        self.labelOutput.setText("")
        self.labelOutput.setObjectName("labelOutput")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 426, 29))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tax Calculator"))
        self.pushButtonCalculate.setText(_translate("MainWindow", "Calculate Tax"))
        self.labelSalary.setText(_translate("MainWindow", "What is your weekly salary?"))
        self.labelDependants.setText(_translate("MainWindow", "How many dependents do you have?"))

