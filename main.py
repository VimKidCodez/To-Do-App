from tkinter import *
from functions import *

root = Tk()
root.title('To-Do List')
root.geometry('300x300')

Label(root, text='To Do List',font=("word",40)).place(x=35, y=10)
tasks = Listbox(root, height=10, width=38)

scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=300, y=300, height=130)

tasks.place(x=30, y=90)

with open('Tasks.txt', 'r+') as tasks_list:
    for task in tasks_list:
        tasks.insert(END, task)
    tasks_list.close()


new_item = Entry(root,width=10)
new_item.place(x=200, y=270)

add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('word', 12),command=lambda: add_item(new_item, tasks))
add_btn.place(x=0, y=265)

delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('word', 12),command=lambda: delete_item(tasks))
delete_btn.place(x=100, y=265)

root.update()
root.mainloop()

