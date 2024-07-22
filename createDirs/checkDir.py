import os

def length():
    entries = os.listdir(r"Store-Product-Management-SPM-main\Data")
        
    return sum(os.path.isdir(os.path.join(r"Store-Product-Management-SPM-main\Data", entry)) for entry in entries)

def usedData():
    with open(r"Store-Product-Management-SPM-main\Data\UsedData.txt", "r") as reader:
        return reader.readlines()
