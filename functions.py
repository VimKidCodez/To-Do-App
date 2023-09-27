from tkinter import *
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()

    listbox.insert(END, new_task)

    with open('tasks.txt', 'a') as tasks_list_file:
        tasks_list_file.write(f'\n{new_task}')


def delete_item(listbox: Listbox):
    listbox.delete(ACTIVE)

    with open('tasks.txt', 'r+') as tasks_list_file:
        lines = tasks_list_file.readlines()

        tasks_list_file.truncate()

        for line in lines:
            if listbox.get(ACTIVE) == line[:-2]:
                lines.remove(line)
            tasks_list_file.write(line)

        tasks_list_file.close()

