from tkinter import *
import os
import shutil
import hashlib
import time

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("账单处理自动化")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('540x270+350+200')
        #set_window_center(self,300,300)
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        '''
        self.init_data_label = Label(self.init_window_name, text="第一步：新增本月文件夹")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="第二步：")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        '''
        self.first_label=Label(self.init_window_name, text="第一步：新增本月文件夹:")
        self.first_label.grid(row=0, column=0)
        self.second_label=Label(self.init_window_name, text="第二步：文件夹内文件名更名:")
        self.second_label.grid(row=1, column=0)
        self.third_label=Label(self.init_window_name, text="第三步：文件夹内文件名更名:")
        self.third_label.grid(row=2, column=0)


        #文本框
        '''
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        '''
        #按钮
        #self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        #self.str_trans_to_md5_button.grid(row=1, column=11)
        self.first_button=Button(self.init_window_name, text="点我", bg="lightblue", width=10,command=self.first_button_click) 
        self.first_button.grid(row=0,column=20)
        self.second_button=Button(self.init_window_name, text="点我", bg="lightblue", width=10) 
        self.second_button.grid(row=1,column=20)

    #功能函数
    def first_button_click(self):
        source_path = os.path.abspath(r'E:\PHY\小陈交接\A业务一部\A每月对账单\A每月对账单\2022年\202206')
        target_path = os.path.abspath(r'E:\PHY\小陈交接\A业务一部\A每月对账单\A每月对账单\2022年\202207')        
        shutil.copytree(source_path,target_path)


'''
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        #print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")




    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)

'''
def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()