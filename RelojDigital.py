import sys
import time
from tkinter import *
def times():
    tiempo_Actual=time.strftime("%H:%M:%S")
    clock.config(text=tiempo_Actual,bg="black",fg="blue",font="Arial 50 bold")
    clock.after(200,times)
root =Tk()
root.geometry("485x250")
root.iconbitmap("logo.ico")
root.title("Reloj Digital con Tkinter")
#Espacio para la hora
clock=Label(root,font=("times",50,"bold"))
clock.grid(row=2,column=1,pady=25,padx=100)
times()
digi=Label(root,text="Hora Actual",font="times 24 bold",fg="red")
digi.grid(row=0,column=1)

root.mainloop()