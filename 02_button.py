from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

btn1 = Button(root, text="버튼1")
btn1.pack() # 윈도우에 버튼 표시

btn2 = Button(root, padx=5, pady=10, text="버튼222222222") # padx, pady는 여백 설정. text 길이에 따라 버튼 사이즈가 가변적
btn2.pack()

btn3 = Button(root, fg="red", bg="yellow", padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4444444444") # width, height는 버튼 사이즈 고정. text가 길면 잘린다.
btn4.pack()

zphoto = PhotoImage(file="C:/DATA_WORKS/PYTHON_WORKS/python_GUI/btn_v.png")
btn5 = Button(root, image=photo)
btn5.pack()

def btncmd():
    print("This Button Works!")

btn6 = Button(root, text="Working Button", command=btncmd)
btn6.pack()

# 창이 닫히지 않도록
root.mainloop()
