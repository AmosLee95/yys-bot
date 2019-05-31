import win32com.client
import os
import tools.scene as scene

# os.system('cd C:/vscode/yysScript/static && regsvr32 dm.dll')
dm = win32com.client.Dispatch('dm.dmsoft')  
print(dm.GetID())

import tools.path

print(tools.path.dirname())