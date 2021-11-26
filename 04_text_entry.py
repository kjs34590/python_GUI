from tkinter import *

root = Tk()
root.title("Nado GUI")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "input text")

e = Entry(root, width=30) # Entry에서는 엔터로 줄바꿈 불가 (ex : 로그인 시 ID, PW 입력)
e.pack()
e.insert(0, "one line only")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1: line 1에서 / 0 : 0번째 컬럼 위치에서
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()

# 창이 닫히지 않도록
root.mainloop()
