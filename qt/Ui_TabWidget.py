# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\python\yys-bot\qt\TabWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(546, 351)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        TabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        TabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        TabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        TabWidget.addTab(self.tab_4, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "页"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "页"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", "页"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_4), _translate("TabWidget", "页"))

