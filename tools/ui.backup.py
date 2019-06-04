import tkinter as tk          # 导入 Tkinter 库
root = tk.Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = tk.Listbox(root)          #  创建两个列表组件
listb2 = tk.Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)
listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
tk.Label(root, 
    text='小工具',    # 标签的文字
    bg='#fff000',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    ).pack()    # 固定窗口位置
root.mainloop()                 # 进入消息循环







