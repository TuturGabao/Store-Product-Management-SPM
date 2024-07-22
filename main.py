import shutil
import os
from createDirs import getname, createDir
from BarCode import AskData, AskName

choice = 0

def remove_n(line):
    length = len(line)
    leng = length - 1
    i = 0
    return_val = ""
    for char in line:
        i += 1
        if i <= leng:
            return_val += char
    
    return return_val

while choice != "exit":
    choice = input("Gen barcode(1) - Read barcode(2) - Reset data folder(3)\nEnter your choice: ")

    try:
        choice = int(choice)
    except Exception:
        if choice != "exit":
            print("Enter a digit...\n")

    if choice == 1:
        name = getname.getName()
        product_name = AskName.get_name()
        data = AskData.get_data()

        createDir.createDir(name)
        createDir.fill_dir(name, data)

    if choice == 2:
        pass

    if choice == 3:
        for item in os.listdir("Data"):
            item_path = os.path.join("Data", item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)

        with open("Data/UsedData.txt", "w") as w:
            w.flush()

        print("Data file reset\n")

        choice = "exit"
