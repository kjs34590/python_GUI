from tkinter import *
import tkinter.messagebox as msgbox # (msgbox 임포트)

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 기차 예매 시스템을 가정
def info():
    msgbox.showinfo("Success", "Your reservation is done.")

def warn():
    msgbox.showwarning("Fail", "The seat is occupied")

def error():
    msgbox.showerror("Error", "Your payment is not completed")

def okcancel():
    msgbox.askokcancel("Ok/Cancel", "This seat is for infants. Are you sure?")

def retrycancel():
    msgbox.askretrycancel("Retry/Cancel", "Temporary Error. Retry?")

def yesno():
    msgbox.askyesno("Yes/No", "This seat is reversed seat. Are you sure?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="Your reservation isn't saved. \n Do you Want to save befor exit?" )
    # Yes : 저장 후 종료
    # NO : 저장하지 않고 종료
    # Cancle : 현재 화면에서 계속 작업
    print("Response : ", response) # True, False, None -> Yes 1, No 0, Etc
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")

Button(root, command=info, text="Success").pack()
Button(root, command=warn, text="Fail").pack()
Button(root, command=error, text="Error").pack()
Button(root, command=okcancel, text="Ok/Cancel").pack()
Button(root, command=retrycancel, text="Retry/Cancel").pack()
Button(root, command=yesno, text="Yes/No").pack()
Button(root, command=yesnocancel, text="Yes/No/Cancel").pack()

root.mainloop()
