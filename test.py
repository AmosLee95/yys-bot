# import win32com.client
# import os
# import tools.scene as scene

# # os.system('cd C:/vscode/yysScript/static && regsvr32 dm.dll')
# dm = win32com.client.Dispatch('dm.dmsoft')  
# print(dm.GetID())

# import tools.path

# print(tools.path.dirname())



import win32gui
import win32api
classname = "MSPaintApp"
titlename = "无标题 - 画图"
#获取句柄
hwnd = win32gui.FindWindow(classname, titlename)
# print(hwnd)
# #获取窗口左上角和右下角坐标
# left, top, right, bottom = win32gui.GetWindowRect(hwnd)






def get_child_windows(parent):        
    '''     
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''     
    if not parent:         
        return      
    hwndChildList = []     
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)          
    return hwndChildList 
print(get_child_windows(hwnd))
#获取某个句柄的类名和标题
title = win32gui.GetWindowText(hwnd)     
clsname = win32gui.GetClassName(hwnd)     

#获取父句柄hwnd类名为clsname的子句柄
hwnd1= win32gui.FindWindowEx(hwnd, None, clsname, None)


win32gui.ShowWindow(hwnd,1)
win32gui.SetActiveWindow(hwnd)


print(1)