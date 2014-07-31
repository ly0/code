 #coding=utf8
import Tkinter
from Tkinter import Tk
import time
import tkFont
from datetime import datetime

FMT = '%H:%M:%S'
FMT_2 = '%y-%m-%d %H:%M:%S'
DUETIME = '18:00:00'

def timedelta(fmt, front_time, last_time):
    delta = datetime.strptime(last_time, fmt) - datetime.strptime(front_time, fmt)
    if delta.days < 0:
        return None
    return str(delta)

class Clock:
    def __init__(self, parent):
        self.parent = parent
        self.initUI()
        self.parent.title('Timer')
        self.parent.after(1000, self.update)
        self.parent.config(bg="black")


    def initUI(self):
        self.ui_frame = Tkinter.Frame(self.parent,bg="black")
        self.ui_frame.grid(row=0, column=0)
 


        self.ui_label1 = Tkinter.Label(self.ui_frame,text="Now: ")
        self.ui_label1.config(bg="black", fg="#5DDE17", font=tkFont.Font(family='Trajan Pro', size=50))
        self.ui_label1.grid(row=0,column=0)
        

        self.ui_label2 = Tkinter.Label(self.ui_frame,text=time.strftime(FMT, time.localtime(time.time())))
        self.ui_label2.config(bg="black", fg="#5DDE17", font=tkFont.Font(family='Trajan Pro', size=120))
        self.ui_label2.grid(row=0, column=1)

        self.ui_label3 = Tkinter.Label(self.ui_frame,text="Leave: ")
        self.ui_label3.config(bg="black", fg="#5DDE17", font=tkFont.Font(family='Trajan Pro', size=50))
        self.ui_label3.grid(row=1,column=0)
        
        now = time.strftime(FMT, time.localtime(time.time()))
        left = timedelta(FMT, now, DUETIME)
        
        self.ui_label4 = Tkinter.Label(self.ui_frame,text=left)
        if left:
            self.ui_label4.config(text=left)
        else:
            left = 'Time\'s up'
        self.ui_label4.config(bg="black", fg="#5DDE17", font=tkFont.Font(family='Trajan Pro', size=120))
        self.ui_label4.grid(row=1, column=1)

        self.ui_label5 = Tkinter.Label(self.ui_frame,text="Today: ")
        self.ui_label5.config(bg="black", fg="#5DDE17", font=tkFont.Font(family='Trajan Pro',size=50))
        self.ui_label5.grid(row=2,column=0)
        
        now = time.strftime(FMT, time.localtime(time.time()))
        left = timedelta(FMT, now, '23:59:59')
        self.ui_label6 = Tkinter.Label(self.ui_frame,text=left)
        self.ui_label6.config(bg="black", fg="#5DDE17", font=tkFont.Font(family='Trajan Pro', size=120))
        self.ui_label6.grid(row=2, column=1)

        self.ui_label7 = Tkinter.Label(self.ui_frame,text="GRE: ")
        self.ui_label7.config(bg="black", fg="#5DDE17", font=tkFont.Font(family='Trajan Pro',size=50))
        self.ui_label7.grid(row=3,column=0)
        
        now = time.strftime('%y-%m-%d %H:%M:%S', time.localtime(time.time()))
        left = timedelta(FMT_2, now, '14-9-13 00:00:00')
        self.ui_label8 = Tkinter.Label(self.ui_frame,text=left)
        self.ui_label8.config(bg="black", fg="#5DDE17", font=tkFont.Font(family='Trajan Pro', size=70))
        self.ui_label8.grid(row=3, column=1)

        self.ui_label9 = Tkinter.Label(self.ui_frame,text="TOEFL: ")
        self.ui_label9.config(bg="black", fg="#5DDE17", font=tkFont.Font(family='Trajan Pro',size=50))
        self.ui_label9.grid(row=4,column=0)
        
        now = time.strftime('%y-%m-%d %H:%M:%S', time.localtime(time.time()))
        left = timedelta(FMT_2, now, '14-10-13 00:00:00')
        self.ui_label10 = Tkinter.Label(self.ui_frame,text=left)
        self.ui_label10.config(bg="black", fg="#5DDE17", font=tkFont.Font(family='Trajan Pro', size=70))
        self.ui_label10.grid(row=4, column=1)
 
        self.ui_label0 = Tkinter.Label(self.ui_frame,text="Extremly Poor")
        self.ui_label0.config(bg="black", fg="#5DDE17", font=tkFont.Font(family='Trajan Pro', size=70, weight='bold'))
        self.ui_label0.grid(row=5,column=0, columnspan=2)  
        
        self.ui_frame.place(anchor="c",relx=.5, rely=.5)  
        self.parent.update()
    def update(self):
        self.ui_label2.config(text=time.strftime('%H:%M:%S', time.localtime(time.time())))
        self.parent.update()
        now = time.strftime(FMT, time.localtime(time.time()))
        left = timedelta(FMT, now, DUETIME)
        if left:
            self.ui_label4.config(text=left)
        else:
            self.ui_label4.config(text='Time\'s up')

        left = timedelta(FMT, now, '23:59:59')
        self.ui_label6.config(text=left)

        now = time.strftime('%y-%m-%d %H:%M:%S', time.localtime(time.time()))
        left = timedelta(FMT_2, now, '14-9-13 00:00:00')
        self.ui_label8.config(text=left)

        now = time.strftime('%y-%m-%d %H:%M:%S', time.localtime(time.time()))
        left = timedelta(FMT_2, now, '14-10-13 00:00:00')
        self.ui_label10.config(text=left)
        self.parent.after(1000, self.update)

root = Tk()
# make it cover the entire screen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
app = Clock(root)

root.mainloop()
