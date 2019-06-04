def  findWindows():
    HwndExLeft = ""
    iMax = len(windowInfoList)
    for windowInfo in windowInfoList
        HwndEx = self.dmPlug.Window.SearchEx(windowInfo(0), 0, 0)
        #TracePrint HwndEx
        windowsList = Split(HwndEx, "|")
        for window in windowsList
            HwndEx2 = self.dmPlug.Window.FindEx(window, 0, windowInfo(1), windowInfo(2))
            
            
            #TracePrint "windowsList("&j&"):"&window
            #TracePrint HwndEx2
            If not HwndEx2 = 0  Then 
                If windowInfo(2) = "MainWindowWindow" Then 
                    #逍遥模拟器，再加两层
                    HwndEx2 = self.dmPlug.Window.FindEx(HwndEx2, 0, "Qt5QWindowIcon", "CenterWidgetWindow")
                    HwndEx2 = self.dmPlug.Window.FindEx(HwndEx2, 0, "Qt5QWindowIcon", "RenderWindowWindow")
                End If
#					TracePrint "add  "& window & "=" & HwndEx2 & "|"
                coord = self.dmPlug.Window.GetClientRect(window)
                    coord_0 = Split(coord, "|")
                TracePrint HwndExLeft
                TracePrint coord
                TracePrint coord_0(0)
                ScreenW = dm.GetScreenWidth()
                ScreenH = dm.GetScreenHeight()
                If Int(coord_0(0)) = ScreenW - 3 + 窗口ID and Int(coord_0(1)) = ScreenH - 1 Then 
                
                    If windowInfo Then 
                        显示窗口
                    End If
                    self.dmPlug.Window.Move window, 窗口ID, 0
                    coord = self.dmPlug.Window.GetClientRect(window)
                    TracePrint "!!!"
                    
                    
                #dm_ret = dm.MoveWindow(window, ScreenW - 3 + 窗口ID, ScreenH - 1)
                #dm_ret = dm.MoveWindow(window,窗口ID,0)
                Else 
                
                TracePrint Int(coord_0(0))
                TracePrint ScreenW - 3 + 窗口ID
                TracePrint Int(coord_0(1))
                TracePrint ScreenH - 1
                End If
                HwndExLeft = HwndExLeft & window & "=" & HwndEx2 & "=" & Replace(coord, "|", "=") & "|"
                #TracePrint ScreenW - 3 + 窗口ID&"   " &ScreenH - 1
            End If
        Next
    Next
    If HwndExLeft = "" Then 
        Goto noWindow
    End If

    TracePrint HwndExLeft
#	排序，根据主窗口的x坐标


    windows = Split(HwndExLeft, "|")
    iMax = len(windows)
    For i = 0 To (iMax - 1)
        
            window_cur1 = Split(windows(i), "=")
        fatherWindow1 = window_cur1(0)
        
            xx1 = Int(window_cur1(2))
        
#	    	TracePrint "xx1"&xx1
        For j = i + 1 To (iMax - 1)
        
            #TracePrint iMax - 1
            
                window_cur2 = Split(windows(j), "=")
            fatherWindow2 = window_cur2(0)
            xx2 = Int(window_cur2(2))
#	    		TracePrint "xx2"&xx2
            If xx1 > xx2 Then 
            #TracePrint 交换
            #交换 
                temp = windows(j)
                windows(j) = windows(i)
                windows(i) = temp
                xx1 = xx2
            End If
        Next
    Next
    HwndExLeft = Join(windows,"|")
    TracePrint HwndExLeft
    findWindows = windows(id)
    If 0 Then 
    Rem noWindow
        findWindows = ""
    End If