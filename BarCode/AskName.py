import tkinter as tk

def returnval():
    global name
    if len(entry.get()) != 0:
        name = entry.get()
        root.quit()

def get_name():
    global entry
    global root
    root = tk.Tk()
    root.geometry("500x70")
    root.title("Product Name")
    root.configure(bg="lightgray")
    root.wm_attributes('-topmost', 1)

    label = tk.Label(root, text="Enter the name of the product:")
    label.place(x=10, y=20, height=20)
    label.configure(bg="lightgray")

    entry = tk.Entry(root)
    entry.place(x=185, y=20, width=200, height=20)

    sub_button = tk.Button(root, text="Submit", command=returnval)
    sub_button.place(x=400, y=15, width=70, height=30) 

    root.mainloop()

    root.destroy()
    root.quit()
    return name