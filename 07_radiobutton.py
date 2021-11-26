from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="choose menu")
label1.pack()

burger_var = IntVar() # 여기에 int형으로 값 저장. radionbutton에서는 하나의 var 공유
btn_burger1 = Radiobutton(root, text="hamburger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="cheeseburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="chickenburger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2 = Label(root, text="choose drink")
label2.pack()

drink_var = StringVar() # 문자형으로 값 저장.
btn_drink1 = Radiobutton(root, text="coke", value="COKE", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="sprite", value="SPRITE", variable=drink_var)
btn_drink3 = Radiobutton(root, text="fanta", value="FANTA", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) # 선택된 항목의 값(value) 반환
    print(drink_var.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

# 창이 닫히지 않도록
root.mainloop()
