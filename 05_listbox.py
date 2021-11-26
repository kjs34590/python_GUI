from tkinter import *

root = Tk()
root.title("Nado GUI")

listbox = Listbox(root, selectmode = "extended", height=0) # extended : 중복 선택 가능(single = 단일 선택) / height : 보여줄 list 개수
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "melon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # 항목 삭제
    # listbox.delete(END) # 맨 뒤 항목 삭제. 0이면 첫 번째 항목 삭제

    # 개수 확인
    print('in this list, there are', listbox.size(), 'fruits.')

    # 항목 확인 (시작 idx, 끝 idx)
    # print('1st~3rd fruits : ', listbox.get(0,2))

    # 선택 항목 확인 (위치로 반환)
    print("selected fruit's index : ", listbox.curselection())

btn = Button(root, text="click", command=btncmd)
btn.pack()

# 창이 닫히지 않도록
root.mainloop()
