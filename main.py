import shutil
import os
from createDirs import getname, createDir
from BarCode import AskData, AskName
import AccessData
import scanner

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

curr_dir = os.getcwd()

while choice != "exit":
    os.chdir(curr_dir)
    choice = input("Gen barcode(1) - Read barcode(2) - Reset data folder(3) \nEnter your choice: ")

    try:
        choice = int(choice)
    except Exception:
        if choice != "exit":
            print("Enter a digit...\n")

    if choice == 1:
        name = getname.getName()
        product_name = AskName.get_name()
        if product_name == "0":
            break
        data = AskData.get_data(product_name)

        createDir.createDir(name)
        createDir.fill_dir(name, data)

    if choice == 2:
        option = input("Get price(1) - Get name(2) - Get description(3) - Get stock(4) - General info(5) \nEnter your choice: ")
        try:
            option = int(option)
        except Exception:
            print("Enter a digit...\n\n")

        if [0, 1, 2, 3, 4, 5].count(option) == 0:
            print("Enter a valid option\n")

        else:
            print("Scan the barcode")
            barcode = scanner.barcode_scanner()
            if barcode != 0:
                if option == 1:
                    if AccessData.get_price(barcode) != 0:
                        print(f"Price of {barcode}: {AccessData.get_price(barcode)}")
                if option == 2:
                    if AccessData.get_name(barcode) != 0:
                        print(f"Name of {barcode}: {AccessData.get_name(barcode)}")
                if option == 3:
                    if AccessData.get_Description(barcode) != 0:
                        print(f"Description of {barcode}: {AccessData.get_Description(barcode)}")
                if option == 4:
                    if AccessData.get_Stock(barcode) != 0:
                        print(f"Stock of {barcode}: {AccessData.get_Stock(barcode)}")
                if option == 5:
                    if AccessData.get_name(barcode) != 0:
                        name = AccessData.get_name(barcode)
                        price = AccessData.get_price(barcode)
                        description = AccessData.get_Description(barcode)

                        print("")
                        print(f"Name: {name}")
                        print(f"Price: {price}")
                        print(f"Description: {description} \n")
            else:
                print("You left the window, restart the process..")

    if choice == 3:
        for item in os.listdir("Donnee"):
            item_path = os.path.join("Donnee", item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)

        with open("Donnee/IDS.txt", "w") as w:
            w.flush()

        with open("Donnee/Names.txt", "w") as w:
            w.flush()

        print("Data file reset\n")

        choice = "exit"
