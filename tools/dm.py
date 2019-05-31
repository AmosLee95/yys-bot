# 提供dm的基本功能：
# 查找窗口
# 绑定窗口
# 点击
# 找图
import win32com.client
# pip install pypiwin32
import os
import time
from path import releasePath
# from tools.path import releasePath
# print(releasePath)
    
if not os.path.exists(releasePath):
    os.mkdir(releasePath)
    os.mkdir(releasePath + '\\plug')
    os.mkdir(releasePath + '\\screenshot')
    os.system('copy %s\\static\\dm.dll %s\\plug\\dm.dll'%(os.path.dirname(os.path.dirname(__file__)),os.path.normcase(releasePath)))
        
    # 注册
    # os.system('cd %s\\plug && regsvr32 dm.dll'%os.path.normcase(releasePath))
print('copy %s\\static\\dm.dll %s\\plug\\dm.dll'%(os.path.dirname(os.path.dirname(__file__)),os.path.normcase(releasePath)))
print('cd %s\\plug\\ && regsvr32 dm.dll'%os.path.normcase(releasePath))

# 注册
# os.system('cd %s\\plug && regsvr32 dm.dll'%os.path.normcase(releasePath))

print(os.path.dirname(os.path.dirname(__file__)) + '\\static')
# os.system('cd C:/vscode/yysScript/static && regsvr32 dm.dll')
class Dm():
    def __init__(self, clientId):
        self.dm = win32com.client.Dispatch('dm.dmsoft')
        self.clientId = clientId
        
        if not os.path.exists(releasePath + '\\screenshot'):
            os.mkdir(releasePath + '\\screenshot')
        self.dm.SetPath(releasePath + '\\screenshot')
        print(self.dm.Ver())
    def findWindow(self):
        # 查找所有的模拟器窗口
        hwnds = []
        print(self.dm.EnumWindow(0,"","LDPlayerMainFrame",1+2+4+8+16))
        if self.dm.EnumWindow(0,"","LDPlayerMainFrame",1+2+4+8+16) =='':
            print('kong')
            return 0
        for hwnd in list(map(int, self.dm.EnumWindow(0,"","LDPlayerMainFrame",1+2+4+8+16).split(","))):
            hwnd2 = self.dm.FindWindowEx(hwnd, "RenderWindow","TheRender")
            hwnd3 = self.dm.FindWindowEx(hwnd2, "subWin","sub")
            self.dm.SetWindowState(hwnd,5)
            rect = self.dm.GetWindowRect(hwnd)
            print('hwnd=%s'%hwnd)
            if hwnd3:
                print('hwnd3=%s'%hwnd3)
                if(rect[0]):
                    # 查找成功
                    x1 = rect[1]
                    y1 = rect[2]
                    x2 = rect[3]
                    y2 = rect[4]
                    print('x1=%s,y1=%s,x2=%s,y2=%s'%(x1,y1,x2,y2))
                hwnds.append({'parentHwnd':hwnd,'SimulatorType':'雷电模拟器','childHwnd':hwnd2,'rect':{'x1':x1,'y1':y1,'x2':x2,'y2':y2}})
        
        # 排序
        def sortKey(item):
            return item['rect']['x1']
        hwnds.sort(key=sortKey)
        print(hwnds)

        # 设置当前ID
        self.hwndInfo = hwnds[self.clientId-1]
        self.parentHwnd = self.hwndInfo['parentHwnd']
        self.childHwnd = self.hwndInfo['childHwnd']
    
    def getWindowState(self):
        # 0 : 判断窗口是否存在
        # 1 : 判断窗口是否处于激活
        # 2 : 判断窗口是否可见
        # 3 : 判断窗口是否最小化
        # 4 : 判断窗口是否最大化
        # 5 : 判断窗口是否置顶
        dm_ret0 = self.dm.GetWindowState(self.parentHwnd,0) 
        dm_ret1 = self.dm.GetWindowState(self.parentHwnd,1) 
        dm_ret2 = self.dm.GetWindowState(self.parentHwnd,2) 
        dm_ret3 = self.dm.GetWindowState(self.parentHwnd,3) 
        dm_ret4 = self.dm.GetWindowState(self.parentHwnd,4) 
        dm_ret5 = self.dm.GetWindowState(self.parentHwnd,5) 
        print("存在:%s 激活:%s 可见:%s 最小化:%s 最大化:%s 置顶:%s"% (dm_ret0,dm_ret1,dm_ret2,dm_ret3,dm_ret4,dm_ret5))
    
    def setWindowState(self):
        ScreenW = self.dm.GetScreenWidth()
        dd = self.dm.GetWindowRect(self.parentHwnd)
        print(dd)
        self.dm.SetWindowState(self.parentHwnd,5)#恢复指定窗口 ,但不激活
        # self.dm.SetWindowState(self.parentHwnd,1)#激活
        # self.dm.MoveWindow(self.parentHwnd,ScreenW - 10 + self.clientId,self.hwndInfo['rect']['y1'] - self.hwndInfo['rect']['y2'] + 5)
        # self.dm.MoveWindow(self.parentHwnd, self.clientId-1, 0)
        # self.dm.MoveWindow(self.childHwnd,0,0)
        # self.dm.SetWindowState(self.parentHwnd,11)# 解除禁止窗口
    def bandWindow(self):
        display = ["gdi","gdi2","dx2","dx3"]
        for dis in display:
            print(dis)
            self.dm.BindWindow(self.childHwnd,dis,"windows","windows",0)
            time.sleep(1)
            self.dm.Capture(0,0,800,600,"screen-"+dis+".bmp")
            if(self.dm.GetAveRGB(0,0,800,600)!="000000"):
                # 不是纯黑，退出
                print("不是纯黑，退出")
                break
            self.dm.UnBindWindow() 
        
    def unBindWindow(self):
        self.dm.UnBindWindow() 
print('sss')
dm = Dm(1)
dm.findWindow()
dm.setWindowState()
# dm = Dm(2)
# dm.findWindow()
# dm.setWindowState()
dm.bandWindow()
dm.unBindWindow()
dm.getWindowState() 
# 获取坐标
# print(dm.dm.GetCursorPos())

# todo
# 思路
# 建立一个dm对象，专门用来检查窗口