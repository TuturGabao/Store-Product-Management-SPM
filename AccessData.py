import json

def get_price(barcode):
    try:
        with open("Donnee/" + barcode + "/data.json", "r") as r:
            data = json.load(r)
            return data.get("Price")
    except Exception:
        print("Invalid barcode!\n")
        return 0

def get_name(barcode):
    try:
        with open("Donnee/" + barcode + "/data.json", "r") as r:
            data = json.load(r)
            return data.get("Name")
    except Exception:
        print("Invalid barcode!\n")
        return 0

def get_ID(barcode):
    try:
        with open("Donnee/" + barcode + "/data.json", "r") as r:
            data = json.load(r)
            return data.get("ID")
    except Exception:
        print("Invalid barcode!\n")
        return 0
    
def get_Description(barcode):
    try:
        with open("Donnee/" + barcode + "/data.json", "r") as r:
            data = json.load(r)
            return data.get("Description")
    except Exception:
        print("Invalid barcode!\n")
        return 0
    
def get_Stock(barcode):
    try:
        with open("Donnee/" + barcode + "/data.json", "r") as r:
            data = json.load(r)
            return data.get("Stock")
    except Exception:
        print("Invalid barcode!\n")
        return 0