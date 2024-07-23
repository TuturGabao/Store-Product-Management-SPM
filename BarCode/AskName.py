import threading
import tkinter as tk

def returnval():
    global name
    name = entry.get()
    if len(entry.get()) != 0:
        if get_Names().count(name + "\n") == 0:
            root.quit()
        else:
            handle_error(0)

def handle_error(error):
    if error == 0:
        error_label.configure(text="Name already used!")

def trigger_thread():
    global timer
    try:
        timer = threading.Timer(3.0, reset_label)
        timer.start()
    except Exception:
        pass

def reset_label():
    error_label.configure(text="")

def get_Names():
    with open("Donnee/Names.txt", "r") as r:
        return r.readlines()

def get_name():
    global entry
    global root
    global name
    global error_label
    root = tk.Tk()
    root.geometry("500x90")
    root.title("Product Name")
    root.configure(bg="lightgray")
    root.wm_attributes('-topmost', 1)

    label = tk.Label(root, text="Enter the name of the product:")
    label.place(x=10, y=20, height=20)
    label.configure(bg="lightgray")

    error_label = tk.Label(root, text="")
    error_label.place(x=10, y=50, height=20, width=500)
    error_label.configure(bg="lightgray")

    entry = tk.Entry(root)
    entry.place(x=185, y=20, width=200, height=20)

    sub_button = tk.Button(root, text="Submit", command=returnval)
    sub_button.place(x=400, y=15, width=70, height=30) 

    root.mainloop()
    try:
        root.destroy()
    except Exception:
        print("You closed the window, please recreate the product")
        name = "0"

    try:
        timer.cancel()
    except Exception:
        pass

    return name