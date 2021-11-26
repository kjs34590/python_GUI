from tkinter import *

root = Tk()
root.title("Nado GUI")

chkvar = IntVar() # chkvar에 int형으로 값을 저장한다.
chkbox = Checkbutton(root, text="Don't show today", variable=chkvar)
chkbox.select() # 자동 선택 처리 (deselect는 선택 해제 처리)
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="Don't show 7 days", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

# 창이 닫히지 않도록
root.mainloop()
