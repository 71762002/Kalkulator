from operatsion import ishoralar

def calculate():
    while True:
        try:
            x = float(input("Birinchi son: "))
        except ValueError:
            print("Raqam kiritilmadi")
        else:
            break

    amal = ishoralar()
    while True:
        try:
            hint = input(f"Birini tanlang {amal['ishora_str']} >> ")
            if hint not in amal['ishora_list']:
                print("Amalni qayta kiriting.")
                continue
        except Exception:
            print("Amal to'g'ri kiritilmadi")
        else:
            break

    while True:
        try:
            y = float(input("Ikkinchi son: "))
        except ValueError:
            print("Raqam kiritilmadi")
        else:
            break

    if hint == "+":
        return x + y
    elif hint == "-":
        return x - y
    elif hint == "/":
        return x / y
    elif hint == "*":
        return x * y




