from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

def create_new_file():
    print("Create New File")

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) # 프로그램 종료

menu.add_cascade(label="File", menu=menu_file)

# Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

# Language 메뉴 추가 (radio 버튼을 통해 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="English")
menu_lang.add_radiobutton(label="Korean")
menu_lang.add_radiobutton(label="French")
menu.add_cascade(label="Language", menu=menu_lang)

# Toolbar 메뉴 추가 (checkbox)
menu_tool = Menu(menu, tearoff=0)
menu_tool.add_checkbutton(label="Select Tools")
menu_tool.add_checkbutton(label="Draw Tools")
menu.add_cascade(label="Tools", menu=menu_tool)

root.config(menu=menu)
# 창이 닫히지 않도록
root.mainloop()
