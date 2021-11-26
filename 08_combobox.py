from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

values = [str(i)+"일" for i in range(1, 32)] # 1~31까지의 숫자

combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")

# 읽기 전용 콤보박스
ro_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
ro_combobox.current(0) # 0번째 인덱스 값 선택
ro_combobox.pack()

def btncmd():
    print(combobox.get())
    print(ro_combobox.get())

btn = Button(root, text="date", command=btncmd)
btn.pack()

# 창이 닫히지 않도록
root.mainloop()
