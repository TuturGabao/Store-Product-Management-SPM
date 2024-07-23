import os

def length():
    entries = os.listdir("Donnee")
        
    return sum(os.path.isdir(os.path.join("Donnee", entry)) for entry in entries)
