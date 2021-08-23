from PyQt5 import QtWidgets 
from PyQt5.QtCore import QTimer

from qt.Ui_main import Ui_MainWindow 
from qt.Ui_scriptTabs import Ui_tabFrame 
from qt.Ui_script import Ui_ScriptControler 
from qt.Ui_noWindow import Ui_NoWindow

from tools.dm import Dm
import sys
import time

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow): 
    def __init__(self, parent = None): 
        super(MainWindow,self).__init__(parent) 
        self.setupUi(self) 
        self.dm = Dm()
        self.windowInfos = self.dm.findWindows()
        
        if len(self.windowInfos) :
            self.addScriptTabs(self.windowInfos)
        else:
            self.info=NoWindow()
            self.gridLayout.addWidget(self.info)
            self.info.show() 
            

    def addScriptTabs(self, windowInfos):
        # 添加tab
        self.scriptTabs=ScriptTabs(windowInfos)
        self.gridLayout.addWidget(self.scriptTabs)
        self.scriptTabs.show() 
    
class NoWindow(QtWidgets.QWidget,Ui_NoWindow): 
    def __init__(self, parent = None): 
        super(NoWindow,self).__init__(parent) 
        self.setupUi(self) 
  
class ScriptTabs(QtWidgets.QWidget,Ui_tabFrame): 
    def __init__(self,windowInfos, parent = None): 
        super(ScriptTabs,self).__init__(parent) 
        self.setupUi(self) 
        self.tabs = []
        for windowInfo in windowInfos:
            self.addTab(self, windowInfo)
    def addTab(self, ScriptTabs, windowInfo):
        # add new tab
        newTab = QtWidgets.QWidget()
        newTab.setObjectName("tab_4")
        self.tabWidget.addTab(newTab, windowInfo['title'])
        self.tabs.append(newTab)
        # add new scriptControler
        gridLayout = QtWidgets.QGridLayout(newTab)
        newScriptControler = ScriptControler(windowInfo)
        gridLayout.addWidget(newScriptControler)
        # newTab.

class ScriptControler(QtWidgets.QWidget,Ui_ScriptControler): 
    def __init__(self, windowInfo, parent = None): 
        super(ScriptControler,self).__init__(parent) 
        self.setupUi(self) 
        self.windowInfo = windowInfo
        self.dm = Dm(windowInfo['fatherHwnd'])
        self.dm.childHwnd = windowInfo['childHwnd']
        self.dm.fatherHwnd = windowInfo['fatherHwnd']
        res = self.dm.tryBandWindow()
        print('绑定成功' if res else '绑定失败！')
        
        self.timer = QTimer(self) #初始化一个定时器
        self.timer.timeout.connect(self.timerFunction) #计时结束调用operate()方法
        self.timer.start(2000) #设置计时间隔并启动
    def timerFunction(self):
        print('zzz...')
        # time.sleep(1)
        self.timer.stop()
def run():
    app=QtWidgets.QApplication(sys.argv) 
    mainWindow=MainWindow() 
    mainWindow.show() 
    sys.exit(app.exec_())
run()