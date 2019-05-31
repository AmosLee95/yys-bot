from dm import Dm
import tkinter as tk          # 导入 Tkinter 库


class MainWin():
    def __init__(self):
        self.root = tk.Tk()                     # 创建窗口对象的背景色
        self.root.title("yys-bot  QQ群567783492")
        self.initializeWin()

    def initializeWin(self):

# todo:清空已有的控件！
# todo2:注意保留还存在的模拟器的控制！
        self.getWindowInfos()
        # 模拟器列表
        uiLabelFramewindowlist = tk.LabelFrame(self.root,width=300, height=18*self.windowNumber+40, text='模拟器列表：')
        uiLabelFramewindowlist.grid(row=0,column=0,padx=15)
        uifr=tk.Frame(width = 300,height=18*self.windowNumber+40)
        uifr.grid(row=0, column=0, columnspan=2)

        print(self.windowInfos)
        windowlist = tk.Listbox(uifr,width=30, height=self.windowNumber)
        for windowInfo in self.windowInfos:
            windowlist.insert(0,windowInfo['title'])
        windowlist.grid(row=0, column=0)

        bottonRun = tk.Button(uifr, text="刷新列表", command=self.initializeWin)  # 创建一个按钮, text
        bottonRun.grid(row=0, column=1,padx=15)
        # 模拟器控制
        windowControl = []
        for i in range(self.windowNumber):
            windowControl.append(tk.LabelFrame(self.root,width=300, height=80, text=self.windowInfos[i]['title']))
            windowControl[i].grid(row=i+1,column=0,padx=15)
            uifr=tk.Frame(width = 300,height = 40, bg='#fff000')
            uifr.grid(row=i+1, column=0,columnspan=2)

            bottonRun = tk.Button(uifr, text="开始")  # 创建一个按钮, text
            bottonRun.grid(row=0, column=0,padx=15)
            bottonRun = tk.Button(uifr, text="配置")  # 创建一个按钮, text
            bottonRun.grid(row=0, column=2, columnspan=2,padx=15)


        self.root.mainloop()                 # 进入消息循环
    def getWindowInfos(self):
        self.dm = Dm()
        self.windowInfos = self.dm.findWindows()
        self.windowNumber = len(self.windowInfos)

MainWin()