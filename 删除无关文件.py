import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_folder(var):
    folder_selected = filedialog.askdirectory()
    var.set(folder_selected)

def delete_unmatched_files():
    image_folder = image_var.get()
    json_folder = json_var.get()
    txt_folder = txt_var.get()

    if not image_folder or not json_folder or not txt_folder:
        messagebox.showwarning("Warning", "Please select all folders.")
        return

    # 获取三个文件夹中的文件名（不包括扩展名）
    image_files = {os.path.splitext(f)[0] for f in os.listdir(image_folder)}
    json_files = {os.path.splitext(f)[0] for f in os.listdir(json_folder)}
    txt_files = {os.path.splitext(f)[0] for f in os.listdir(txt_folder)}

    # 找到共同的文件名
    common_files = image_files.intersection(json_files, txt_files)

    # 删除不在共同文件名中的文件
    for folder, files in [(image_folder, image_files), (json_folder, json_files), (txt_folder, txt_files)]:
        for filename in files:
            if filename not in common_files:
                file_path = os.path.join(folder, filename + os.path.splitext(next(f for f in os.listdir(folder) if f.startswith(filename)))[1])
                os.remove(file_path)
                print(f'Deleted: {file_path}')

    messagebox.showinfo("Info", "Deletion process completed.")

# 创建主窗口
root = tk.Tk()
root.title("File Cleaner")

# 定义文件夹路径变量
image_var = tk.StringVar()
json_var = tk.StringVar()
txt_var = tk.StringVar()

# 创建并布局界面组件
tk.Label(root, text="Image Folder:").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=image_var, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=lambda: select_folder(image_var)).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="JSON Folder:").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=json_var, width=50).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=lambda: select_folder(json_var)).grid(row=1, column=2, padx=10, pady=5)

tk.Label(root, text="TXT Folder:").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=txt_var, width=50).grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=lambda: select_folder(txt_var)).grid(row=2, column=2, padx=10, pady=5)

# 添加删除按钮
tk.Button(root, text="Delete Unmatched Files", command=delete_unmatched_files).grid(row=3, column=1, padx=10, pady=20)

# 运行主循环
root.mainloop()
