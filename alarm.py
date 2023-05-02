from tkinter import *
import datetime
import time
from pygame import mixer
import threading
from tkinter import messagebox
root =Tk()
root.title("Alarm Clock")
root.geometry("530x330")
alarmtime=StringVar()
msqi=StringVar()
head=Label(root,text="Alarm Clock",font=('comic sans',18))
head.grid(row=0,columnspan=7,pady=4)
mixer.init()

def ala():
     a=alarmtime.get()

     Alarmt=a
     CurrentTime=time.strftime("%H:%M")

     while Alarmt!=  CurrentTime:
           CurrentTime=time.strftime("%H:%M")
     if Alarmt==CurrentTime:
        mixer.music.load('alarm.mp3')
        mixer.music.play()
        msg=messagebox.showinfo('Info',f'{msqi.get()}')
        if msg=='ok':
             mixer.music.stop()

Clockimg = PhotoImage(file= "ai.png")
img = Label(root,image=Clockimg)
img.grid(rowspan=4,column =0)

inputt=Label(root,text="Input time",font=('Arial',15))
inputt.grid(row=1,column =3)

altime=Entry(root,textvariable=alarmtime,font=("comic sans",18),width=6)
altime.grid(row=1,column=2)

msg=Label(root,text="Message",font=("comic sans",18))
msg.grid(row=4,columnspan=5)
msqinput=Entry(root,textvariable=msqi,font=('comic sans',18))
msqinput.grid(row=5,column=1,columnspan=2)
submit=Button(root,text="SUBMIT ",font=('comic sans',18),command=ala)
submit.grid(row=7,column=2,columnspan=2)

root.mainloop()