import createDirs.checkDir as checkDir
import random

nums = checkDir.length()
usedData = checkDir.usedData()

def _to13digits(num):
    nums = str(num)
    while len(nums) != 13:
        nums = "0" + nums
    return nums


def getName():
    if nums >= 9999999999999:
        print("Memory exceeded")
        return "Error 1"
    
    else:
        while True:
            name = random.randint(1, 9999999999999)
            if name not in usedData:
                return _to13digits(name)