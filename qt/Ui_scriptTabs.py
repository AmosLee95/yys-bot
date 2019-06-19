# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\python\yys-bot\qt\ui\scriptTabs.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tabFrame(object):
    def setupUi(self, tabFrame):
        tabFrame.setObjectName("tabFrame")
        tabFrame.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(tabFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(tabFrame)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(tabFrame)
        QtCore.QMetaObject.connectSlotsByName(tabFrame)

    def retranslateUi(self, tabFrame):
        _translate = QtCore.QCoreApplication.translate
        tabFrame.setWindowTitle(_translate("tabFrame", "Frame"))

