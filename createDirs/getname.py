import createDirs.checkDir as checkDir
import random

nums = checkDir.length()

def calculate_ean13_check_digit(number):
    if len(number) != 12 or not number.isdigit():
        raise ValueError("Number must be exactly 12 digits long and contain only digits")

    total = 0
    for i, digit in enumerate(number):
        if i % 2 == 0:
            total += int(digit)
        else:
            total += int(digit) * 3

    check_digit = (10 - (total % 10)) % 10
    return check_digit

def add_check_digit(number):
    check_digit = calculate_ean13_check_digit(number)
    return number + str(check_digit)

def _to12digits(num):
    nums = str(num)
    while len(nums) != 12:
        nums = "0" + nums
    return nums


def getName():
    if nums >= 9999999999999:
        print("Memory exceeded")
        return "Error 1"
    
    else:
        name = random.randint(1, 999999999999)
        name = _to12digits(name)
        name = add_check_digit(str(name))
        return name
            