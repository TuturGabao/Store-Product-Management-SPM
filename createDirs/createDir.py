import os
import json
from BarCode import QrcodeGen

def createDir(name):
    os.chdir("Donnee/")
    os.mkdir(name)

def fill_dir(dir_name, data):
    data["Barcode"] = dir_name
    with open(dir_name + "/data.json", "w") as w:
        json.dump(data, w)

    with open("IDS.txt", "a") as a:
        a.write(str(data.get("ID")) + "\n")

    with open("Names.txt", "a") as a:
        a.write(str(data.get("Name")) + "\n")

    QrcodeGen.generate_barcode(dir_name, dir_name + "/" + dir_name)
