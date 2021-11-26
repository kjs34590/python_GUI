from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

progressbar = ttk.Progressbar(root, maximum = 100, mode="indeterminate")
progressbar.start(10) # 10ms마다 움직임
progressbar.pack()

# determinate
progressbar2 = ttk.Progressbar(root, maximum = 100, mode="determinate")
progressbar2.start(10) # 10ms마다 움직임
progressbar2.pack()

# 
p_var3 = DoubleVar() # Doublevar : 실수 값 반영
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var3)
progressbar3.pack()

def btncmd1():
    progressbar.stop() # 작동 중지
    progressbar2.stop() # 작동 중지

def btncmd2():
    for i in range(101):
        time.sleep(0.02)

        p_var3.set(i)
        progressbar3.update()
        print(p_var3.get())

btn = Button(root, text="stop", command=btncmd1)
btn2 = Button(root, text="start", command=btncmd2)
btn.pack()
btn2.pack()

# 창이 닫히지 않도록
root.mainloop()
