from barcode import EAN13
from barcode.writer import ImageWriter

def generate_barcode(number, file_name):
    with open(file_name + ".jpeg", "wb") as f:
        EAN13(number, writer=ImageWriter()).write(f)

