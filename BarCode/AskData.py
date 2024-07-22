import tkinter as tk
import threading


DATA = {

}

def reset_label():
    error_label.configure(text="")
    

def trigger_thread():
    timer = threading.Timer(3.0, reset_label)
    timer.start()

def add_Data(key, value):
    value_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)

    if len(key) == 0:
        error_label.configure(text="Please enter the info name")
        trigger_thread()
        return
        
    if len(value) == 0:
        error_label.configure(text="Please enter the info value")
        trigger_thread()
        return
        
    try:
        value = int(value)
        DATA[key] = value
    except Exception:
        if value.lower() == "true" or value.lower() == "false":
            DATA[key] = bool(value)
        else:
            DATA[key] = value

    print(DATA)

def get_data():
    global error_label
    global key_entry
    global value_entry

    root = tk.Tk()
    root.geometry("420x300")
    root.title("Data Saver")

    root.configure(bg="lightgray")

    key_label = tk.Label(root, text="Info Name")
    key_label.place(x=30, y=20, width=100, height=20)
    key_label.configure(bg="lightgray")
    key_entry = tk.Entry(root)
    key_entry.place(x=30,y=50,width=100,height=20)

    value_label = tk.Label(root, text="Info Value")
    value_label.place(x=160, y=20, width=100, height=20)
    value_label.configure(bg="lightgray")
    value_entry = tk.Entry(root)
    value_entry.place(x=160,y=50,width=100,height=20)

    submit_button = tk.Button(root, text="Submit", command=lambda:add_Data(key_entry.get(), value_entry.get()))
    submit_button.place(x=290, y=50, width=100, height=20)
    submit_button.configure(bg="lightgray")

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.place(x=180, y=100, width=60, height=20)

    error_label = tk.Label(root, text="")
    error_label.place(x=30, y=160, width=360, height=30)
    error_label.configure(bg="lightgray")

    root.mainloop()
    root.destroy()
    return DATA