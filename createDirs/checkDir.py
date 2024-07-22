import os

def length():
    return len(next(os.walk('Data'))[1])

def usedData():
    with open("Data/UsedData.txt", "r") as reader:
        return reader.readlines()