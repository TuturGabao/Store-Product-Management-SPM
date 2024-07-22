import os
import json
from BarCode import QrcodeGen
import createDirs.checkDir as checkDir

usedData = checkDir.usedData()

def createDir(name):
    os.chdir(r"Data")
    os.mkdir(name)

def _to13digits(num):
    nums = str(num)
    while len(nums) != 13:
        nums = "0" + nums
    return nums

def writeData(data):
    dat = _to13digits(data)
    with open("Data/UsedData.txt", "w") as w:
        lines = usedData
        w.writelines(lines)
        w.write(dat + "\n")
    
def fill_dir(dir_name, data):
    base_path = r"Data"
    file_name = "data.json"
    full_path = os.path.join(base_path, dir_name, file_name)
    with open(full_path, "w") as w:
        json.dump(data, w, indent=4)

    QrcodeGen.generate_barcode(dir_name, full_path)
    writeData(dir_name)
    
