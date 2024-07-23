import tkinter as tk
import threading

DATA = {

}

def reset_label():
    try:
        error_label.configure(text="")

        value_entry_des1.configure(background="lightgray")
        value_entry_ID1.configure(background="lightgray")
        value_entry_prix1.configure(background="lightgray")
        value_entry_stock1.configure(background="lightgray")
    except Exception:
        pass
    
def trigger_thread():
    global timer
    try:
        timer = threading.Timer(3.0, reset_label)
        timer.start()
    except Exception:
        pass

def get_ids():
    ids = []
    with open("Donnee/IDS.txt", "r") as r:
        lines = r.readlines()

        for line in lines:
            try:
                ids.append(int(line))
            except Exception:
                pass
        return ids
    
def submit(name):
    bad = True
    if value_entry_stock.get() == "":
        value_entry_stock1.configure(background="red")
        error_label.configure(text="Enter the number of stock")
        bad = False
    if value_entry_prix.get() == "":
        value_entry_prix1.configure(background="red")
        error_label.configure(text="Enter the price of the product")
        bad = False
    if value_entry_des.get() == "":
        value_entry_des1.configure(background="red")
        error_label.configure(text="Enter the description of the product")
        bad = False
    if value_entry_ID.get() == "":
        value_entry_ID1.configure(background="red")
        error_label.configure(text="Enter the ID number")
        bad = False
    
    des = value_entry_des.get()
    ID = value_entry_ID.get()
    prix = value_entry_prix.get()
    stock = value_entry_stock.get()

    if bad:
        try:
            stock=int(stock)
        except Exception:
            error_label.configure(text="Stock should be a number")
            value_entry_stock1.configure(background="red")
            bad = False

        try:
            prix=float(prix)
        except Exception:
            error_label.configure(text="Price should be a number")
            value_entry_prix1.configure(background="red")
            bad = False

        try:
            ID=int(ID)
        except Exception:
            error_label.configure(text="ID should be a number")
            value_entry_ID1.configure(background="red")
            bad = False

    if get_ids().count(ID) != 0:
        bad = False
        error_label.configure(text="ID already used")
        value_entry_ID1.configure(background="red")

    if not bad:
        trigger_thread()
    else:
        DATA["ID"] = ID
        DATA["Name"] = name
        DATA["Description"] = des
        DATA["Price"] = prix
        DATA["Stock"] = stock

        root.quit()
    

def get_data(name):
    global root
    global DATA
    global error_label

    global value_entry_des
    global value_entry_ID
    global value_entry_prix
    global value_entry_stock

    global value_entry_des1
    global value_entry_ID1
    global value_entry_prix1
    global value_entry_stock1

    DATA = {

    }

    root = tk.Tk()
    root.geometry("420x350")
    root.title("Data Saver")

    root.configure(bg="lightgray")

    key_label_ID = tk.Label(root, text="ID")
    key_label_ID.place(x=30, y=50, width=100, height=20)
    key_label_ID.configure(bg="lightgray")

    key_label_des = tk.Label(root, text="Description")
    key_label_des.place(x=30, y=80, width=100, height=20)
    key_label_des.configure(bg="lightgray")

    key_label_prix = tk.Label(root, text="Prix")
    key_label_prix.place(x=30, y=110, width=100, height=20)
    key_label_prix.configure(bg="lightgray")

    key_label_stock = tk.Label(root, text="Quantité en stock")
    key_label_stock.place(x=30, y=140, width=100, height=20)
    key_label_stock.configure(bg="lightgray")

    value_label = tk.Label(root, text="Info Value")
    value_label.place(x=160, y=20, width=100, height=20)
    value_label.configure(bg="lightgray")

    value_entry_ID1 = tk.Label(root)
    value_entry_ID1.place(x=159,y=49,width=102,height=22)

    value_entry_ID = tk.Entry(root)
    value_entry_ID.place(x=160,y=50,width=100,height=20)

    value_entry_des1 = tk.Label(root)
    value_entry_des1.place(x=159,y=79,width=102,height=22)

    value_entry_des = tk.Entry(root)
    value_entry_des.place(x=160,y=80,width=100,height=20)

    value_entry_prix1 = tk.Label(root)
    value_entry_prix1.place(x=159,y=109,width=102,height=22)

    value_entry_prix = tk.Entry(root)
    value_entry_prix.place(x=160,y=110,width=100,height=20)

    value_entry_stock1 = tk.Label(root)
    value_entry_stock1.place(x=159,y=139,width=102,height=22)

    value_entry_stock = tk.Entry(root)
    value_entry_stock.place(x=160,y=140,width=100,height=19)

    submit_button = tk.Button(root, text="Submit", command=lambda:submit(name))
    submit_button.place(x=290, y=140, width=100, height=20)
    submit_button.configure(bg="lightgray")

    error_label = tk.Label(root, text="")
    error_label.place(x=30, y=160, width=360, height=30)
    error_label.configure(bg="lightgray")

    root.mainloop()
    try:
        root.destroy()
    except Exception:
        print("You closed the window, please recreate the product")
        
    try:
        timer.cancel()
    except Exception:
        pass
    return DATA

