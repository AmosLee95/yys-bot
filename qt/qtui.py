from PyQt5 import QtWidgets 
# try:
#     from ui.Ui_main import Ui_MainWindow 
#     from ui.Ui_scriptTabs import Ui_tabFrame 
#     from ui.Ui_script import Ui_ScriptControler 
# except ModuleNotFoundError:
from qt.ui.Ui_main import Ui_MainWindow 
from qt.ui.Ui_scriptTabs import Ui_tabFrame 
from qt.ui.Ui_script import Ui_ScriptControler 
  
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow): 
    def __init__(self, parent = None): 
        super(MainWindow,self).__init__(parent) 
        self.setupUi(self) 
        if True :
            self.addScriptTabs()
    def addScriptTabs(self):
        # 添加tab
        self.scriptTabs=ScriptTabs(5)
        self.gridLayout.addWidget(self.scriptTabs)
        self.scriptTabs.show() 
  
class ScriptTabs(QtWidgets.QWidget,Ui_tabFrame): 
    def __init__(self,num, parent = None): 
        super(ScriptTabs,self).__init__(parent) 
        self.setupUi(self) 
        self.tabs = []
        for i in range(num):
            self.addTab(self, "模拟器#%d"%(i+1))
    def addTab(self, ScriptTabs, title):
        # add new tab
        newTab = QtWidgets.QWidget()
        newTab.setObjectName("tab_4")
        self.tabWidget.addTab(newTab, title)
        self.tabs.append(newTab)
        # add new scriptControler
        gridLayout = QtWidgets.QGridLayout(newTab)
        newScriptControler = ScriptControler()
        gridLayout.addWidget(newScriptControler)
        # newTab.

class ScriptControler(QtWidgets.QWidget,Ui_ScriptControler): 
    def __init__(self, parent = None): 
        super(ScriptControler,self).__init__(parent) 
        self.setupUi(self) 




def run():
    import sys 
    app=QtWidgets.QApplication(sys.argv) 
    mainWindow=MainWindow() 
    mainWindow.show() 
    sys.exit(app.exec_())
# run()