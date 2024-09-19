from tkinter import *
from datetime import datetime, timedelta
import tkinter.font as tkFont
from PIL import Image, ImageTk

Window = Tk()
Window.title("Digital Watch - Tehran Time")
Window.geometry('240x100')
Window.attributes('-alpha', 0.7)  
Window.overrideredirect(False) 

Window.resizable(True, True)


img = Image.new('RGB', (800, 600), (0, 0, 0))
photo = ImageTk.PhotoImage(img)
background_label = Label(Window, image=photo)
background_label.place(relwidth=1, relheight=1)

digital_font = tkFont.Font(family="Times New Roman", size=60)


def mytime():
   
    tehran_time = datetime.utcnow() + timedelta(hours=3, minutes=30)
    hour = tehran_time.strftime('%I')
    minute = tehran_time.strftime('%M')
    second = tehran_time.strftime('%S')
    Am_Pm = tehran_time.strftime("%p")
    DAY = tehran_time.strftime("%A")
    DATE = tehran_time.strftime("%Y-%m-%d")  

    MYtext = f"{hour}:{minute}:{second} {Am_Pm}"
    MYtext2 = f"{DAY}, {DATE} - Tehran"  

    font_size = int(60 * Window.winfo_height() / 350)  
    digital_font.configure(size=font_size)

   
    MyLabel.config(text=MYtext, font=digital_font, fg='cyan', bg=None)  
    MyLabel2.config(text=MYtext2, font=("Arial", font_size - 30), fg='white', bg=None)  

    MyLabel.after(1000, mytime)

MyLabel = Label(Window, bg='black', bd=0)  
MyLabel2 = Label(Window, bg='black', bd=0)  
MyLabel.pack(pady=20)
MyLabel2.pack()

mytime()
Window.mainloop()
