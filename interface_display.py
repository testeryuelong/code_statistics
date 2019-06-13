#encoding:utf-8

from count_code import count_aciton
from tkinter import *

def show():
    """读取输入内容，将结果显示在结果展示text中"""
    result = count_aciton.judge(e.get())
    if isinstance(result,str):
        text.insert(END,result)
    elif isinstance(result,dict):
        for key,value in result.items():
            text.insert(END,("{0}文件的代码行数为{1}行".format(key,value)))
            text.insert(END,"\n")
            text.see(END)
            text.update()  # 实时更新插入日志
        text.insert(END,"所有文件的代码行数共计{0}行".format(str(sum(result.values()))))

def empty():
    """清空输入框和结果展示框"""
    e.delete(0, END)
    text.delete(0.0, END)
	

window =Tk()
window.title('代码统计工具')
window.geometry('500x400')

#框架布局
frame_root = Frame(window)
frame1 = Frame(frame_root)

Label(frame_root, text="输入目标路径：", font=("Arial", 15), width=20, height=2,).grid(padx=10,pady=10)

#输入框设置
value=StringVar()
value.set("")
e=Entry(frame_root,textvariable=value)
e.grid(ipadx=80,ipady=5,pady=10)


#子布局，使button控件在一行显示
Button(frame1, text="提交", font=("Arial", 12), width=5, height=2,fg='black',command=show,justify="center").grid(row=5, column=0,padx=10,pady=10)
Button(frame1, text="清空", font=("Arial", 12), width=5, height=2,fg='black',command=empty,justify="center").grid(row=5, column=1,padx=10,pady=10)
Button(frame1, text="退出", font=("Arial", 12), width=5, height=2,fg='black',command=window.quit,).grid(row=5, column=2,padx=10,pady=10)
frame1.grid()


Label(frame_root, text="结果展示如下：", font=("Arial", 15), width=20, height=2,justify="center").grid(padx=5,pady=5)
frame_root.pack()

#结果展示不在frame中
text = Text(window,width=50, height=10,)
text.pack()

window.mainloop()   #激活窗口
