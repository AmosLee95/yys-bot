# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\python\yys-bot\qt\noWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NoWindow(object):
    def setupUi(self, NoWindow):
        NoWindow.setObjectName("NoWindow")
        NoWindow.resize(693, 300)
        self.widget = QtWidgets.QWidget(NoWindow)
        self.widget.setGeometry(QtCore.QRect(150, 90, 351, 32))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(NoWindow)
        QtCore.QMetaObject.connectSlotsByName(NoWindow)

    def retranslateUi(self, NoWindow):
        _translate = QtCore.QCoreApplication.translate
        NoWindow.setWindowTitle(_translate("NoWindow", "Form"))
        self.label_2.setText(_translate("NoWindow", "模拟器支持列表：雷电模拟器/夜神模拟器/MUMU模拟器"))
        self.label.setText(_translate("NoWindow", "没发现任何模拟器窗口，请先打开模拟再打开yys-bot"))

