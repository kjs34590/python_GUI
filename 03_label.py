from tkinter import *

root = Tk()
root.title("Nado GUI")

label1 = Label(root, text="Hello")
label1.pack()

photo = PhotoImage(file="C:/DATA_WORKS/PYTHON_WORKS/python_GUI/btn_v.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="See you again")

    global photo2
    photo2 = PhotoImage(file="C:/DATA_WORKS/PYTHON_WORKS/python_GUI/btn_x.png")
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

# 창이 닫히지 않도록
root.mainloop()
