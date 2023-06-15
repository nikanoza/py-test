import re
pattern = r"^(?=[A-Za-z]{2})[A-Za-z]{2}(?:[A-Za-z]{0,3}[1-9]|[1-9][A-Za-z0-9]{0,4})$"
pattern_2 = r"^[A-Za-z]+[0-9]+[A-Za-z]+$"

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    match = re.match(pattern, s) and not re.match(pattern_2, s)
    return match

main()