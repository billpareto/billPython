from cProfile import label
from cgitb import text
import datetime
from fileinput import filename
import string
from tkinter import *
import os
import shutil
import glob
import time
from tkinter import filedialog
from tkinter import messagebox
from turtle import left
from unicodedata import name

def makefilename():
        d=datetime.date.today()
        n=datetime.datetime.now()
        s="Video"+str(d.year)+str(d.month)+str(d.day)+str(n.hour)+str(n.minute)+str(n.second)
        return s


class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("视频提取小助手")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('500x150+350+200')
        #set_window_center(self,300,300)
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        
        #标签
        
        self.first_label=Label(self.init_window_name, text="第一步：请设置保存后的视频名称及目录：")
        self.first_label.grid(row=0, column=0,sticky='w')
        self.filename_lable=Label(self.init_window_name,text="名称：")
        self.filename_lable.grid(row=1,column=0,sticky='w')
        self.filename_lable=Label(self.init_window_name,text=".MP4")
        self.filename_lable.place(x=250,y=25,anchor=NW)
        self.filepath_lable=Label(self.init_window_name,text="目录：")
        self.filepath_lable.grid(row=2,column=0,sticky='w')
        self.second_label=Label(self.init_window_name, text="第二步：请点击\"准备提取\"后打开需要提取的视频，然后返回本程序")
        self.second_label.grid(row=3, column=0,sticky='w')
        self.third_label=Label(self.init_window_name, text="第三步：观看完成前10秒内，点击按钮提取:")
        self.third_label.grid(row=4,column=0,sticky='w')

        #文本框
        
        self.filename_entry=Entry(self.init_window_name,width=30)
        self.filename_entry.place(x=40,y=25,anchor=NW)
        self.filename_entry.insert(0,makefilename())
        self.filepath_entry=Entry(self.init_window_name,width=50)
        self.filepath_entry.place(x=40,y=50,anchor=NW)
        self.filepath_entry.insert(0,os.path.join(os.path.expanduser("~"), 'Desktop'))
        
        #按钮
        
        self.first_button=Button(self.init_window_name, text="...",width=8,command=self.first_button_click) 
        self.first_button.place(x=400,y=45,anchor=NW)
        self.second_button=Button(self.init_window_name, text="提取",state='disabled',width=8,command=self.second_button_click) 
        self.second_button.place(x=400,y=105,anchor=NW)
        self.third_button=Button(self.init_window_name, text="准备提取",width=8,command=self.third_button_click) 
        self.third_button.place(x=400,y=75,anchor=NW)

        #菜单 
        self.menu=Menu(self.init_window_name)
        self.menu.add_command(label="关于")
        self.init_window_name['menu']=self.menu


        
        self.filepath=os.path.join(os.path.expanduser("~"), "AppData\\Roaming\\Tencent\\WeChat\\xweb\\web_ng\\Cache")        
        self.filepathD=self.filepath_entry.get()
        self.isvideo = False
        self.file=''
        self.fileD=''

    #功能函数

    



    def first_button_click(self):#设置文件目录
        filepath=filedialog.askdirectory()  
        self.filepath_entry.insert(0,filepath)
        
    def third_button_click(self):
        for root, dirs, files in os.walk(self.filepath, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        self.third_button.configure(state='disabled') 
        self.first_button.configure(state='disabled') 
        self.second_button.configure(state='normal')   

    def second_button_click(self):#提取视频文件
        
        if self.filename_entry.get()=='':
            messagebox.showinfo("消息","文件名不可为空")
            return
        if self.filepath_entry.get()=="":
            messagebox.showinfo("消息","保存目录不可为空")
            return
        
        

        for filename in os.listdir(self.filepath):
            self.file=self.filepath+'\\'+filename
            
            if filename.startswith("f_") and os.stat(self.file).st_mtime>time.time()-50 and os.stat(self.file).st_size/1024>2000:
                self.fileD=self.filepathD+"\\"+self.filename_entry.get()+".mp4"
                break
        
        try:
            shutil.copyfile(self.file,self.fileD)
        except PermissionError:
            messagebox.showinfo("消息","稍候再试，谢谢")
            return
        else:
            messagebox.showinfo("消息","恭喜提取成功！！！")
            self.filename_entry.delete(0,END)
            self.filename_entry.insert(0,makefilename())            
            self.second_button.configure(state='disabled') 
            self.isvideo = True
                
        if not self.isvideo:
            messagebox.showinfo("消息","提取失败,请在视频结束前点击提取按钮，谢谢")
            #print(os.path.basename(file))
            #print(os.stat(filepath+'\\'+file))
        self.third_button.configure(state='normal') 
        self.first_button.configure(state='normal') 
        #messagebox.showinfo("消息","提取成功！！！")
        


def gui_start():
    init_window = Tk()              #实例化出一个父窗口    
    filename_var = StringVar()
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()