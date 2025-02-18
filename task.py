 استيراد للمكتبة دي المكتبة دي ياسارة يتعمل شنو بتعرض لينا الواجهة عشان ندخل فيها المهمات #
اسم المكتبة Tinker #
import tkinter as tk
from tkinter import ttk
 
tasks = []   دي عبارة عباره عن مصفوفة فارغة ي سارة بعدين بنضيف فيها العناصر #
#داله اضافة الممهمة
def add_task():
    task = task_entry.get()   دي داله ي ساررة وظيفتها شنو تشيل الحاجة الدخلتها #
    if task:  هنا عملنا شرط نعرف هل في مهمة كتبت في الصندوق#
        tasks.append(task)    هتا يتضيف العناصر للقائمة ديك بتاع المصفوفة #
        update_task_list()       بعض ماضفنا عملنا تحدبث للمدخلات #
        task_entry.delete(0, tk.END) بعدين نمسح مربع الاضافة #
#دالة حذف المهمة
def delete_task():    
    try:
        task_index = task_listbox.curselection()[0]  عشان نجيب الموقع الحالي #
        tasks.pop(task_index) اذا دايرنين نحذف مهمة#
        update_task_list()  بعض ماضفنا عملنا تحدبث للمدخلات #
    except IndexError:
        pass  # لا يوجد مهمة محددة لحذفها
دالة واظيقنها تجديث المدخلات 
def update_task_list():
    task_listbox.delete(0, tk.END) نمسج العنصر من القائمة 
    for task in tasks:   عمل لوب لكل العناصر في القائمة#
        task_listbox.insert(tk.END, task) ادخل العناصر#






هنا نشغل الداوال الفوق دييك#
root = tk.Tk() عشان نغرض الواجهة#
root.title("Task Manager") دا العنوان طبعا#

task_label = ttk.Label(root, text="Task:")   للعرض العنوان ا#
task_label.grid(row=0, column=0, padx=5, pady=5)  تصميم تخطيط#

task_entry = ttk.Entry(root) حندخل البيانات في الصندوف#
الوجب افهمي ديل#
task_entry.grid(row=0, column=1, padx=5, pady=5)

add_button = ttk.Button(root, text="Add Task", command=add_task) 
add_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

task_listbox = tk.Listbox(root, height=10)
task_listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

delete_button = ttk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

update_task_list()  

root.mainloop()
