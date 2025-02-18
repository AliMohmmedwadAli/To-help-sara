import tkinter as tk
from tkinter import ttk

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        tasks.pop(task_index)
        update_task_list()
    except IndexError:
        pass  # لا يوجد مهمة محددة لحذفها

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

root = tk.Tk()
root.title("Task Manager")

task_label = ttk.Label(root, text="Task:")
task_label.grid(row=0, column=0, padx=5, pady=5)

task_entry = ttk.Entry(root)
task_entry.grid(row=0, column=1, padx=5, pady=5)

add_button = ttk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

task_listbox = tk.Listbox(root, height=10)
task_listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

delete_button = ttk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

update_task_list()  

root.mainloop()