def main():
    while True:
        try:
            user_input = input("Fraction: ")
            a,b = user_input.split("/")
            if int(a) == int(b) and int(a) > 0:
                print("F")
                break
            if int(a) == 0 and int(b) > 0:
                print("E")
                break
            result = int(a) / int(b) * 100
            print(f"{int(result)}%")
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue

main()

