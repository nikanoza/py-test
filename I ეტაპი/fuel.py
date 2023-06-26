def main():
    while True:
        try:
            user_input = input("Fraction: ")
            result = fuel(user_input)
            print(result)
            if result == "F":
                print("F")
                break
            if result == "E":
                print("E")
                break
            print(f"{int(result)}%")
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue

def fuel(str):
    a,b = str.split("/")
    if int(a) == int(b) and int(a) > 0:
        return "F"
    if int(a) == 0 and int(b) > 0:
        return"E"
    result = int(a) / int(b) * 100
    return int(result)

if __name__ == "__main__":
    main()

