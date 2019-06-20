# 提供dm的基本功能：
# 查找窗口
# 绑定窗口
# 点击
# 找图
# 隐藏窗口
# 显示窗口
import win32com.client
# pip install pypiwin32
import os
import time
import math
import random
# try:
#     from config import supportList
#     from path import releasePath
# except:
from tools.config import supportList
from tools.path import releasePath
print("random() : ", random.random())
print("random() : ", random.random())
print("random() : ", random.random())
print("random() : ", random.random())
print("random() : ", random.random())
# from tools.path import releasePath
print(releasePath)
    
if not os.path.exists(releasePath):
    os.mkdir(releasePath)
    os.mkdir(releasePath + '\\plug')
    os.mkdir(releasePath + '\\screenshot')
    os.system('copy %s\\static\\dm.dll %s\\plug\\dm.dll'%(os.path.dirname(os.path.dirname(__file__)),os.path.normcase(releasePath)))
        
    # 注册
    # os.system('cd %s\\plug && regsvr32 dm.dll'%os.path.normcase(releasePath))
# print('copy %s\\static\\dm.dll %s\\plug\\dm.dll'%(os.path.dirname(os.path.dirname(__file__)),os.path.normcase(releasePath)))
# print('cd %s\\plug\\ && regsvr32 dm.dll'%os.path.normcase(releasePath))

# 注册
# os.system('cd %s\\plug && regsvr32 dm.dll'%os.path.normcase(releasePath))

# print(os.path.dirname(os.path.dirname(__file__)) + '\\static')
# os.system('cd C:/vscode/yysScript/static && regsvr32 dm.dll')
def delay(time0):
    print("delay:%d==>%f"%(time0,time0/1000))
    time.sleep(time0/1000)


delay(123)

class Dm():
    def __init__(self, clientId=0):
        self.dmPlug = win32com.client.Dispatch('dm.dmsoft')
        self.clientId = clientId
        
        if not os.path.exists(releasePath + '\\screenshot'):
            os.mkdir(releasePath + '\\screenshot')
        self.dmPlug.SetPath(releasePath + '\\screenshot')
        # print(self.dmPlug.Ver())

    def  findWindows(self):
        windowInfos = []
        for supportInfo in supportList:
            fatherHwndEx = self.dmPlug.EnumWindow(0,0,supportInfo[0],31)
            print(supportInfo)
            print( fatherHwndEx)
            # print("dddd:%s"%fatherHwndEx)
            fatherHwndList = fatherHwndEx.split(",")
            if fatherHwndEx == "":
                # 没找到，跳过
                continue
            for fatherHwnd in fatherHwndList:
                # print('fatherHwnd:%s'%fatherHwnd)
            #     fatherHwnd2 = int(fatherHwnd)
                childHwndEx = self.dmPlug.EnumWindow(fatherHwnd, supportInfo[2], supportInfo[1],31)
                # print(childHwndEx)
                if childHwndEx == "":
                    # 没找到，跳过
                    continue
                childHwnd = childHwndEx.split(",")[0]
                # print( childHwnd)
                self.fatherHwnd = fatherHwnd
                self.childHwnd = childHwnd
                coord = self.dmPlug.GetClientRect(fatherHwnd)
                # print(coord)
                self.setWindowState()
                self.getWindowState()
                
                coord = self.dmPlug.GetClientRect(fatherHwnd)
                # print(coord)
                if(coord[0]!=1):
                    # print('coord[0]!=1 !!')
                    while(1):
                        pass
                # 如果坐标为负数，则移动起来！
                # screenW = self.dmPlug.GetScreenWidth()
                # screenH = self.dmPlug.GetScreenHeight()
                flag = True
                i = 0
                for i in range(len(windowInfos)):
                    windowInfo = windowInfos[i]
                    if windowInfo['coord'][1] > coord[1]:
                        # 插入
                        windowInfos.insert(i, {
                            'fatherHwnd':fatherHwnd,
                            'childHwnd':childHwnd,
                            'coord':coord,
                            'title':self.dmPlug.GetWindowTitle(fatherHwnd)
                        })
                        flag = False
                        break
                if flag:
                    # 插入
                    # todo:改成goto
                    windowInfos.insert(len(windowInfos), {
                        'fatherHwnd':fatherHwnd,
                        'childHwnd':childHwnd,
                        'coord':coord,
                        'title':self.dmPlug.GetWindowTitle(fatherHwnd)
                    })
                # print('windowInfos')
                # print(windowInfos)
            if len(windowInfos) == 0:
                print("没找到窗口！")
        return windowInfos
                
    def getWindowState(self):
        res = []
        for i in range(6):
            res.append(self.dmPlug.GetWindowState(self.fatherHwnd,i) )
        # print("存在:%s 激活:%s 可见:%s 最小化:%s 最大化:%s 置顶:%s"% (res[0],res[1],res[2],res[3],res[4],res[5]))
        return res
    
    def setWindowState(self):
        # ScreenW = self.dmPlug.GetScreenWidth()
        dd = self.dmPlug.GetWindowRect(self.fatherHwnd)
        # print(dd)
        self.dmPlug.SetWindowState(self.fatherHwnd,5)#恢复指定窗口 ,但不激活
        self.dmPlug.SetWindowState(self.fatherHwnd,1)#激活
        # self.dmPlug.MoveWindow(self.fatherHwnd,ScreenW - 10 + self.clientId,self.hwndInfo['rect']['y1'] - self.hwndInfo['rect']['y2'] + 5)
        # self.dmPlug.MoveWindow(self.fatherHwnd, self.clientId-1, 0)
        # self.dmPlug.MoveWindow(self.childHwnd,0,0)
        # self.dmPlug.SetWindowState(self.fatherHwnd,11)# 解除禁止窗口
    def bandWindow(self, display, mouse, keypad, mode):
        self.dmPlug.BindWindow(self.childHwnd, display, mouse, keypad, mode)
    def tryBandWindow(self):
        display = ["gdi","gdi2","dx2","dx3"]
        for dis in display:
            # print(dis)
            self.dmPlug.BindWindow(self.childHwnd,dis,"windows","windows",0)
            time.sleep(1)
            self.dmPlug.Capture(0,0,800,600,"screen-"+dis+".bmp")
            if(self.dmPlug.GetAveRGB(0,0,800,600)!="000000"):
                # 不是纯黑，退出
                # print("不是纯黑，退出")
                return True
                break
            self.dmPlug.UnBindWindow() 
        return False
    def unBindWindow(self):
        self.dmPlug.UnBindWindow() 

    def click(self,x, y, rMax):
        print( "          myClick: " & x & ", " & y)
        if x>=0 and y >=0 and  x<=800 and y <=600:
            pi = 3.1415926535897932
            
            r = random.random() * rMax
            angle =  random.random() * 2 * pi
            x2 = math.cos(angle) * r
            y2 = math.sin(angle) * r
            
            self.dmPlug.MoveTo(x + x2, y + y2)
            self.dmPlug.LeftDown()
            delay(30 + random.random() * 20)
            self.dmPlug.LeftUp()
            delay(300 + random.random() * 20)

# dm = Dm(1)
# dm.findWindows()